from django.shortcuts import render, redirect
from .models import Products, Category
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

# product_index 페이지
@login_required
def seller_index(request):
    products = Products.objects.filter(user=request.user)
    context={
        'object_list': products
    }
    return render(request, 'seller/seller_products_index.html', context)

# 상품 등록
@login_required
def add_products(request):
    if request.method=='GET':
        return render(request=request, template_name='seller/seller_add_products.html')

    elif request.method=='POST':

        user = request.user
        category = Category.objects.get(name=request.POST['category'])
        products_name = request.POST['name']
        products_price = request.POST['price']
        products_description = request.POST['description']

        # 이미지 저장 및 url 설정 내용
        fs=FileSystemStorage()
        uploaded_file = request.FILES['file']
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        
        Products.objects.create(user=user, category=category, name=products_name, price=products_price , description=products_description, image_url=url)        
        return redirect('seller:seller_index')   

# 상품 상세
@login_required
def products_detail(request, pk):
    object = Products.objects.get(pk=pk)
    context = {
        'object':object
    }
    return render(request, 'seller/seller_products_detail.html', context)

# 상품 삭제
@login_required
def delete_products(request, pk):
    object = Products.objects.get(pk=pk)
    object.delete()
    return redirect('seller:seller_index')  
