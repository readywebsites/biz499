from django.shortcuts import render,redirect,get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Category,Blog_Post,Pricecard,Portfolio,Team
from marketing.models import Subscription,New_Project,Open_posts,Home_logos,Home_services,Lead
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Count,Q


def get_category_count():
  queryset = Blog_Post\
    .objects\
    .values('categories__title') \
    .annotate(Count('categories__title'))
  return queryset

def get_port_category_count():
  queryset = Portfolio\
    .objects\
    .values('filter_category__title') \
    .annotate(Count('filter_category__title'))
  return queryset

  
def search(request):
  category_count = get_category_count()
  category_list = Category.objects.all()
  bloglist = Blog_Post.objects.all().order_by('-publish_date')
  query = request.GET.get('q')

  if query:
    bloglist = bloglist.filter(
      Q(title__icontains = query) |
      Q(overview__icontains = query) |
      Q(meta_description__icontains = query) |       
      Q(meta_keywords__icontains = query) |      
      Q(meta_title__icontains = query) |      
      Q(meta_author__icontains = query)|        
      Q(categories__title__icontains = query)     
    ).distinct()

  paginator = Paginator(bloglist,1)
  page_request_variable = 'page'
  page = request.GET.get(page_request_variable)
  try:
    paginated_queryset = paginator.page(page)
  except EmptyPage:
    paginated_queryset = paginator.page(2)
  except PageNotAnInteger:
    paginated_queryset = paginator.page(1)

  latest = Blog_Post.objects.order_by('-publish_date')[0:3]
  portfolio_latest = Portfolio.objects.all()[0:6]
  context = {   
    'category_count' : category_count,
    'bloglist' : paginated_queryset,
    'page_request_variable' : page_request_variable,
    'latest':latest,
    'query':query,
    'category_list':category_list,
    'portfolio_latest':portfolio_latest,
  }


  return render(request,'search_result.html',context)



def index(request):
  # project = Blog_Post.objects.filter (project = True)
  # project_latest = Blog_Post.objects.filter (project = True).order_by ('-Timestamp')[0:3]
  home_services = Home_services.objects.all()
  home_logos = Home_logos.objects.all()
  team_members = Team.objects.order_by('pk')[0:4]
  latest = Blog_Post.objects.order_by ('-Timestamp')[0:3]
  pricecard = Pricecard.objects.all()
  selected_work_list = Portfolio.objects.filter (selected_work = True)
  full_work_list = Portfolio.objects.all()
  # latest_only_blog = Blog_Post.objects.exclude (project = True).order_by ('-Timestamp')[0:3]
  if request.method == 'POST' :
    if 'email_sub' in request.POST:
      email = request.POST['email']
      subscriber = Subscription()
      subscriber.email = email
      subscriber.save()
      messages.success(request, "You have successfully subscribed to our mailing list")
      return HttpResponseRedirect('/contacts')
    
    else:
      full_name = request.POST['full_name']
      contact_number =  request.POST['contact_number']
      message = request.POST['message']
      lead = Lead()
      lead.full_name = full_name
      lead.contact_number = contact_number
      lead.message = message
      lead.save()
      messages.success(request,"Thankyou for reaching us out! Our team shall contact you soon! ")
      return HttpResponseRedirect('/portfolio')

  context = {
    'team_members' : team_members,
    # 'project_list' : project,
    'selected_work_list' : selected_work_list,
    'full_work_list': full_work_list,
    'latest' : latest,
    'pricecard' : pricecard,
    'home_services' : home_services,
    'home_logos' : home_logos,

    # 'latest_blog' : latest_only_blog,
  }
  return render(request,'index.html',context)




def blog(request):
  category_list = Category.objects.all()
  portfolio_latest = Portfolio.objects.all()[0:6]
  category_count = get_category_count()
  bloglist = Blog_Post.objects.all().order_by('-publish_date')
  paginator = Paginator(bloglist,1)
  page_request_variable = 'page'
  page = request.GET.get(page_request_variable)
  try:
    paginated_queryset = paginator.page(page)
  except EmptyPage:
    paginated_queryset = paginator.page(2)
  except PageNotAnInteger:
    paginated_queryset = paginator.page(1)
  
  selected_work_list = Portfolio.objects.filter (selected_work = True)
  latest = Blog_Post.objects.order_by ('-publish_date')[0:3]


  context = {
    'category_list' : category_list,
    'category_count' : category_count,
    'selected_work_list':selected_work_list,
    'portfolio_latest':portfolio_latest,
    'bloglist' : paginated_queryset,
    'page_request_variable' : page_request_variable,
    'latest':latest,
  }
  return render(request,'blog.html',context)

def post(request,slug):
  post = get_object_or_404(Blog_Post,new_blog_slug=slug)
  latest = Blog_Post.objects.order_by ('-publish_date')[0:3]
  latest_projects = Portfolio.objects.all()[0:6]

  context= {
    'post':post,
    'latest':latest,
    'latest_projects':latest_projects,
  }
  return render(request,'blog-single.html',context)


def portfolio(request):
  portfolio_list = Portfolio.objects.all()
  portfolio_total = Portfolio.objects.all().count()
  latest = Blog_Post.objects.order_by ('-Timestamp')[0:3]
  selected_work_list = Portfolio.objects.filter (selected_work = True)

  port_category_count = get_port_category_count()
  context={
    'latest':latest,
    'selected_work_list':selected_work_list,
    'portfolio_list':portfolio_list,
    'port_category_count':port_category_count,
    'portfolio_total':portfolio_total

  }
  return render(request,'portfolio.html',context)

def portfolio_detail(request,slug):
  portfolio_detail = get_object_or_404(Portfolio,new_portfolio_slug=slug)
  latest = Blog_Post.objects.order_by ('-Timestamp')[0:3]
  selected_work_list = Portfolio.objects.filter (selected_work = True)
  portfolio_list = Portfolio.objects.all()
  context={    
    'portfolio_detail':portfolio_detail,
    'latest':latest,
    'selected_work_list':selected_work_list,
    'portfolio_list':portfolio_list
  }
  return render(request,'portfolio-single-v2.html',context)

def about(request):
  home_logos = Home_logos.objects.all()
  team_members = Team.objects.all()
  context={
    'home_logos':home_logos,
    'team_members':team_members
  }
  return render(request,'about.html',context)

