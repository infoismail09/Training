from django.http import HttpResponse

######### Function Based middleware implementation ############

# def my_middleware(get_response):
#     print("One Time Initialization")
#     def my_function(request):
#         print("This is Before View")
#         response = get_response(request)
#         print("This is after view")
#         return response
#     return my_function



########## implementing multiple middleware ############


# class BrotherMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print("One time Brother Initialization")

#     def __call__(self,request):
#         print("This is Brother before view")
#         response = self.get_response(request)
#         print("This is Brother after the views")
#         return response
    

# class FatherMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print("One time Father Initialization")

#     def __call__(self,request):
#         print("This is Father before view")
#         response = self.get_response(request) # iske mtlb  bhai next middleware ko dekhega nahi toh view ke pass jayega 
#         # response = HttpResponse('Nikal lo')
#         print("This is Father after the views")
#         return response
    

# class MotherMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print("One time Mother Initialization")

#     def __call__(self,request):
#         print("This is Mother before view")
#         response = self.get_response(request)  # iske mtlb  bhai next middleware ko dekhega nahi toh view ke pass jayega 
#         print("This is Mother after the views")
#         return response




 
 #### Middleware Hooks are special methods for classed based middlware only: ####


class MyProcessMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    def process_view(request,*args, **kwargs):
        print("This is process view - Before view")
        # return HttpResponse("This is before View") 
        return None # iss case me abhi view chalega 



    
########## Exception Middelware ############


# class MyExceptionMiddleware:
#     def __init__(self,get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         response = self.get_response(request)
#         return response
    
#     def process_exception(self,request,exception):
#         print("Exception Occur")
#         msg = exception 
#         class_name = exception.__class__.__name__
#         print(class_name)
#         print(msg)
#         return HttpResponse(msg)


######### Template Hookh Middleware ###########

# class MyTemplateResponseMiddleware:
#     def __init__(self,get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         response = self.get_response(request)
#         return response
    
#     def process_template_response(self,request,response):
#         print("Process Template Response Middleware")
#         response.context_data['name'] = 'sabir'
#         return response
    
    

############# class based middleware Implementation ################


# class MyMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print("One time Initialization")

#     def __call__(self,request):
#         print("This will execute before view")
#         response = self.get_response(request)
#         print("this will execute after the views")
#         return response

        