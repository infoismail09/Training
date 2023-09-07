from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init,post_init,pre_save,post_save,pre_delete,post_delete,pre_migrate,post_migrate
from django.core.signals import request_started,request_finished,got_request_exception
from django.db.backends.signals import connection_created

@receiver(user_logged_in, sender=User)  #another way to connect siganal with decorator
def login_success(sender, request, user, **kwargs):
    print("##----------------------------------##")
    print("Logged-in Signal ... run INtro..")
    print("Sender:", sender)
    print("request:", request)
    print("User:", user)
    print("User Password:", user.password)
    print(f'kwargs: {kwargs}')
# user_logged_in.connect(login_success, sender=User)


@receiver(user_logged_out, sender=User)  #another way to connect siganal with decorator
def log_out(sender, request, user, **kwargs):
    print("##----------------------------------##")
    print("log_out Signal ... run outro..")
    print("Sender:", sender)
    print("request:", request)
    print("User:", user)
    print(f'kwargs: {kwargs}')
# user_log_out.connect(log_out, sender=User)


@receiver(user_login_failed)  #another way to connect siganal with decorator
def login_failed(sender, credentials, request, **kwargs):
    print("##----------------------------------##")
    print("login_failed Signal ... Failed ..")
    print("Sender:", sender)
    print("Credentials:", credentials)
    print("request:", request)
    print(f'kwargs: {kwargs}')
# user_login_failed.connect(login_failed, sender=User)


@receiver(pre_save, sender=User)
def at_beginning_save(sender, instance, **kwargs):
    print("##----------------------------------##")
    print("pre Save Signal ...")
    print("Sender:", sender)
    print("Instance:", instance)
    print(f'kwargs: {kwargs}')
# pre_save.connect(at_beginning_save, sender=User)


@receiver(post_save, sender=User)
def at_beginning_save(sender, instance, created,**kwargs):
    if created:
        print("##----------------------------------##")
        print("post save Signal ...")
        print('New Record')
        print("Sender:", sender)
        print("Instance:", instance)
        print("Created:", created)
        print(f'kwargs: {kwargs}')
    else:
        print("##----------------------------------##")
        print("post save Signal ...")
        print('New Record')
        print("Sender:", sender)
        print("Instance:", instance)
        print("Created:", created)
        print(f'kwargs: {kwargs}')
# post_save.connect(at_beginning_save, sender=User)


@receiver(pre_delete, sender=User)
def at_beginning_delete(sender, instance, **kwargs):
    print("##----------------------------------##")
    print("pre delete Signal ...")
    print("Sender:", sender)
    print("Instance:", instance)
    print(f'kwargs: {kwargs}')
# pre_delete.connect(at_beginning_delete, sender=User)

@receiver(post_delete, sender=User)
def at_ending_delete(sender, instance, **kwargs):
    print("##----------------------------------##")
    print("post delete Signal ...")
    print("Sender:", sender)
    print("Instance:", instance)
    print(f'kwargs: {kwargs}')
# post_delete.connect(at_ending_delete, sender=User)



@receiver(pre_init, sender=User)
def at_beginning_init(sender, *args, **kwargs):
    print("##----------------------------------##")
    print("Pre Init signal...")
    print("Sender:", sender)
    print(f'Args: {args}')
    print(f'kwargs: {kwargs}')
# pre_init.connect(at_beginning_init, sender=User)



@receiver(post_init, sender=User)
def at_ending_init(sender, *args, **kwargs):
    print("##----------------------------------##")
    print("post Init signal...")
    print("Sender:", sender)
    print(f'Args: {args}')
    print(f'kwargs: {kwargs}')
# post_init.connect(at_ending_init, sender=User)


@receiver(request_started)
def at_begning_request(sender, environ, **kwargs):
    print("##----------------------------------##")
    print("At begning request...")
    print("Sender:", sender)
    print("Environ:", environ)
    print(f'kwargs: {kwargs}')
# request_started.connect(at_begning_request)

@receiver(request_finished)
def at_ending_request(sender, **kwargs):
    print("##----------------------------------##")
    print("At Ending request...")
    print("Sender:", sender)
    print(f'kwargs: {kwargs}')
# request_finished.connect(at_ending_request)

@receiver(got_request_exception)
def at_req_exception(sender, request, **kwargs):
    print("##----------------------------------##")
    print("At request Exception...")
    print("Sender:", sender)
    print("Request:", request)
    print(f'kwargs: {kwargs}')
# got_request_exception.connect(at_req_exception)

@receiver(pre_migrate)
def before_install_app(sender, app_config, verbosity,interactive,using,plan,apps,**kwargs):
    print("##----------------------------------##")
    print("Before install app ...")
    print("Sender:", sender)
    print("App_Config:", app_config)
    print("Verbosity:", verbosity)
    print("Interactive:", interactive)
    print("Using:", using)
    print("Plan:", plan)
    print("App:", apps)
    print(f'kwargs: {kwargs}')
# pre_migrate.connect(before_install_app)


@receiver(post_migrate)
def at_end_migrate_flush(sender, app_config, verbosity,interactive,using,plan,apps,**kwargs):
    print("##----------------------------------##")
    print("at_end_migrate_flush...")
    print("Sender:", sender)
    print("App_Config:", app_config)
    print("Verbosity:", verbosity)
    print("Interactive:", interactive)
    print("Using:", using)
    print("Plan:", plan)
    print("App:", apps)
    print(f'kwargs: {kwargs}')
# post_migrate.connect(at_end_migrate_flush)


@receiver(connection_created)
def Connec_db(sender, connection, **kwargs):
    print("##----------------------------------##")
    print("Initial Connection to the data base...")
    print("Sender:", sender)
    print("Connection:", connection)
    print(f'kwargs: {kwargs}')
# connection_created.connect(Connec_db)
