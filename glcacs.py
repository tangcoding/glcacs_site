""" imports """
import os
import urllib
import json
import csv

import webapp2

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext import ndb
from google.appengine.api import mail

import time
import datetime
from random import randint
from urlparse import urlparse

import webpage_template as tp

from google.appengine.api import images


""" routes """

class Routes_handler(webapp2.RequestHandler):
    def get(self):
        # - page url
        page_address = self.request.uri
        path_layer = urlparse(page_address)[2].split('/')[1]
        base = os.path.basename(page_address)

# - get user
        user = users.get_current_user()
        if user:
            login_key = users.create_logout_url(self.request.uri)
            gate =  'Logout'
            user_name = user.nickname()

        else: # - logged out
          login_key = users.create_login_url(self.request.uri)
          gate = 'Sign in'
          user_name = ''

# - public user

        # default page template
        nav_object = tp.public_navbar_html
        page_id = 'home'
        page_name = 'Home'
        page_html = tp.home_page_html
        carousel_lg = tp.carousel_lg
        page_class = 'public'
        text_template = ''
        data_type = ''


        if path_layer == 'about_us':
            page_id = 'about_us'
            page_name = 'About US'
            page_html = tp.about_us_page_html

        if path_layer == 'conference':
            page_id = 'conference'
            page_name = 'Conference'
            page_html = tp.conference_page_html

        if path_layer == 'conference_registration':
            page_id = 'conference_registration'
            page_name = 'Registration'
            page_html = tp.conf_registration_page_html

            if base == 'thankyou':
                page_id = 'registration_thankyou'
                page_name = 'Thank You'
                page_html = tp.registration_thankyou_page_html    

            if base == 'check_registration':
                page_id = 'check_registration'
                page_name = 'Check Registration'
                page_html = tp.check_registration_page_html  

            if base == 'submit_form':
                page_id = 'submit_form'
                page_name = 'Submit Abstract Form'
                page_html = tp.login_page_html  

                if user:
                    page_html = tp.submit_abstract_page_html

            if base == 'abs_data':      
                page_id = 'abs_data'
                page_name = 'View Abstract Data'
                page_html = tp.login_page_html  

                if user:
                    page_html = tp.abs_data_page_html

        if path_layer == 'activities':
            page_id = 'activities'
            page_name = 'Activities'
            page_html = tp.activities_page_html

        if path_layer == 'jobs':
            page_id = 'jobs'
            page_name = 'Sponsors and Jobs'
            page_html = tp.jobs_page_html

        if path_layer == 'contact':
            page_id = 'contact'
            page_name = 'Contact US'
            page_html = tp.contact_page_html

            if base == 'thankyou':
                page_id = 'comment_thankyou'
                page_name = 'Thank You'
                page_html = tp.contact_thankyou_page_html  

      # - // manage pages
        if path_layer == 'manage':
            nav_object = tp.manage_navbar_html
            page_id = 'login_page'
            page_name = 'Manage'
            page_html = tp.login_page_html
            page_class = 'manage'

# - admin user
            if users.is_current_user_admin():

                if base == 'manage':
                    nav_object = tp.manage_navbar_html
                    page_id = 'manage'
                    page_name = 'Manage'
                    page_html = tp.login_page_html
                    page_class = 'manage'

                if base == 'publish_photo':
                    nav_object = tp.manage_navbar_html
                    page_id = 'publish_photo'
                    page_name = 'Publish Photos'
                    page_html = tp.publish_photo_page_html
                    page_class = 'manage'

                if base == 'publish_icon':
                    nav_object = tp.manage_navbar_html
                    page_id = 'publish_icon'
                    page_name = 'Publish Icons'
                    page_html = tp.publish_icon_page_html
                    page_class = 'manage'

                if base == 'publish_job':
                    nav_object = tp.manage_navbar_html
                    page_id = 'publish_job'
                    page_name = 'Publish Jobs'
                    page_html = tp.publish_job_page_html
                    page_class = 'manage'

                if base == 'publish_conference':
                    nav_object = tp.manage_navbar_html
                    page_id = 'publish_conference'
                    page_name = 'Publish Conference Info'
                    page_html = tp.publish_conference_page_html
                    page_class = 'manage'

                if base == 'registration_data':
                    nav_object = tp.manage_navbar_html
                    page_id = 'registration_data'
                    page_name = 'Manage Registration Data'
                    page_html = tp.registration_data_page_html
                    page_class = 'manage'

                if base == 'job_data':
                    nav_object = tp.manage_navbar_html
                    page_id = 'job_data'
                    page_name = 'View Job Data'
                    page_html = tp.job_data_page_html
                    page_class = 'manage'

                if base == 'conference_data':
                    nav_object = tp.manage_navbar_html
                    page_id = 'conference_data'
                    page_name = 'View Conference Data'
                    page_html = tp.conference_data_page_html
                    page_class = 'manage'

                if base == 'photo_data':
                    nav_object = tp.manage_navbar_html
                    page_id = 'photo_data'
                    page_name = 'View Photos Data'
                    page_html = tp.photo_data_page_html
                    page_class = 'manage'              

                if base == 'modify_event':
                    nav_object = tp.manage_navbar_html
                    page_id = 'modify_event'
                    page_name = 'Modify Upcoming Event'
                    #page_html = tp.modify_event_page_html
                    page_html = ''
                    page_class = 'manage' 
                    text_template = tp.event_template_html
                    data_type = 'event'

                if base == 'modify_conference':
                    nav_object = tp.manage_navbar_html
                    page_id = 'modify_registration'
                    page_name = 'Modify Registration Page'
                    page_html = ''
                    page_class = 'manage'     
                    text_template = tp.conf_registration_template_html
                    data_type = 'conference_registration'


# - admin user end

       # -template object

        template_values  = {

            'login_key': login_key,
            'gate': gate,
            'user_name': user_name,
            'page_class': page_class,

          # -
            'path_layer': path_layer,
            'page_name': page_name,
            'page_id': page_id,
            'page_html': page_html,

            'nav_object': nav_object,
            'carousel_lg': carousel_lg,
            'text_template': text_template,
            'data_type': data_type
        }
      # - render
        path = os.path.join(os.path.dirname(__file__), 'PublicSite.html')
        self.response.out.write(template.render(path, template_values))


# - specific for the activities photo page
class Activity_photo_page(webapp2.RequestHandler):
    def get(self,s):
        page_address = self.request.uri
        path_layer = urlparse(page_address)[2].split('/')[1]
        base = os.path.basename(page_address)

        catagory = base

        nav_object = tp.public_navbar_html
        page_id = 'activity_photos'
        page_name = 'Activity Photos'
        page_html = tp.activity_photos_page_html
        page_class = 'public'

        #item = db.Query(Photo_db).filter('year =', year).filter('event_type=', event_type).get()

# - template
        template_values = {

            'page_class': page_class,
            'path_layer': path_layer,
            'page_name': page_name,
            'page_id': page_id,
            
            'page_html': page_html,
            #'item': item,
            'nav_object': nav_object,
            'catagory' : catagory,
        }

      # - render
        #path = os.path.join(os.path.dirname(__file__), 'html/%s.html') %html_file  # point the path and name for the template file
        path = os.path.join(os.path.dirname(__file__), 'PublicSite.html')
        self.response.out.write(template.render(path, template_values))


# - registration related database 

class ConfForm_db(ndb.Model):
    addTime = ndb.DateTimeProperty(auto_now_add=True)
    data_id = ndb.StringProperty()

    name = ndb.StringProperty()
    email = ndb.StringProperty()
    affiliation = ndb.StringProperty()
    comments = ndb.StringProperty()

    @classmethod
    def _get_registration_data(self):

        q = ConfForm_db.query(projection=[ConfForm_db.data_id, ConfForm_db.name, ConfForm_db.email, ConfForm_db.affiliation, ConfForm_db.comments])
        db_data = []
        for result in q.iter():
            db_data.append({'data_id': result.data_id, 'name': result.name, 'email': result.email, 'affiliation': result.affiliation, 'comments': result.comments})

        return json.dumps(db_data)


class Add_ConfForm_db(webapp2.RequestHandler):
    def post(self):

        #- add registration data to db
        date_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        data_id = date_time + '_' + str(randint(0,1000))
        item = ConfForm_db(id=data_id)
        item.data_id = data_id 

        item.name = self.request.get('name')
        item.email = self.request.get('email')
        item.affiliation = self.request.get('affiliation')
        item.comments = self.request.get('comments')

        item.put()
        time.sleep(1)

        #- send confirmation email
        message = mail.EmailMessage(sender="GLCACS <gxfc1616@gmail.com>",
                            subject="Your have registred to the conference")

        message.to = "tangwenjie@utexas.edu"
        message.body = '''
      

        Your have registred to the conference.

        Please let us know if you have any questions.

        GLCACS
        '''

        message.send()
        self.redirect('/conference_registration/thankyou')


class Create_csv(webapp2.RequestHandler):
    def get(self):
        db_data = ConfForm_db.query().order(ConfForm_db.data_id).fetch(projection=['data_id',  'name', 'email', 'affiliation', 'comments'])
        #db_data.order("data_id")

        self.response.headers['Content-Type'] = 'application/csv'
        self.response.headers['Content-Disposition'] = 'attachment; filename=registration_data.csv'

        writer = csv.writer(self.response.out)
        writer.writerow(["Add_Date", "Name","Email", "Affiliation","Comments"])

        for item in db_data:
            writer.writerow([item.data_id, item.name, item.email, item.affiliation, item.comments])

class Find_registration(webapp2.RequestHandler):
    def post(self):

        # - convert angular request to json 
        request_data = json.loads(self.request.body)
        email = request_data.get('email')
        data_id = request_data.get('confirmation_num')
        #print 'lala:',email, data_id

        item = ConfForm_db.query(ConfForm_db.data_id == data_id).get()
        #print 'lala:', item

        msg = {'msg': 'No informaiton found for this combination.'}
        
        if item:
            if item.email == email:
                msg = {'msg': 'You have registred for the conference.'}

        #print 'lala:', msg
            
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(msg))    

class Abs_db(db.Model):

    user_id = db.StringProperty()
    data_id = db.StringProperty()
    name = db.StringProperty()
    email = db.StringProperty()
  # -
    abs_file = db.BlobProperty()

    @classmethod
    def get_data(self):
        user = users.get_current_user()
        if users.is_current_user_admin():
            db_data = db.Query(Abs_db, projection=('user_id', 'data_id', 'email', 'name'))

            data = []
            for f in db_data:
                data.append(db.to_dict(f))
            print 'lala:', data
            return json.dumps(data)

        elif users.get_current_user():
            user_id = users.get_current_user().user_id()
            db_data =db.Query(Abs_db, projection=('data_id', 'email', 'name')).filter('user_id = ', user_id)

            data = []
            for result in db_data:
                data.append({'user_id': user_id, 'data_id': result.data_id, 'email': result.email,  'name': result.name})
            print 'lala:', data
            return json.dumps(data)    

class Add_Abs_db(webapp2.RequestHandler):
    def post(self):
        user_id = users.get_current_user().user_id()
        item = Abs_db.get_by_key_name(user_id)
        #print 'lala:',user_id


        if item:
            item.name  = self.request.get('name')
            item.data_id = self.request.get('confirmation_num')
            if self.request.get('abs_file'):
                item.abs_file = self.request.get('abs_file')
        else:           
            item = Abs_db(key_name=user_id)
            item.user_id = user_id 
            item.email = users.get_current_user().email()
            item.name  = self.request.get('name')
            item.data_id = self.request.get('confirmation_num')

            if self.request.get('abs_file'):
                item.abs_file = self.request.get('abs_file')

        item.put()
        time.sleep(1)
        self.redirect('/conference_registration/abs_data')

# job info related database

class Job_db(db.Model):

    user_id = db.UserProperty()
    data_id = db.StringProperty()
    job_info = db.StringProperty()
    post_date = db.StringProperty()
  # -
    job_info_file = db.BlobProperty()

class Add_Job_db(webapp2.RequestHandler):
    def post(self):
        date_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        data_id = date_time + '_' + str(randint(0,1000))
        item = Job_db(key_name=data_id)
        item.data_id = data_id 

        if users.is_current_user_admin():

            item.user_id = users.get_current_user()

        item.job_info = self.request.get('job_info')
        item.post_date = self.request.get('post_date')
        item.job_info_file = self.request.get('job_info_file')

        item.put()
        time.sleep(1)
        self.redirect('/manage/job_data')


# conference info related database

class Confinfo_db(db.Model):

    user_id = db.UserProperty()
    data_id = db.StringProperty()
    year = db.StringProperty()
    datetime = db.StringProperty()
    location = db.StringProperty()
    theme = db.StringProperty()
    organizer = db.StringProperty()
    att1_name = db.StringProperty()
    att2_name = db.StringProperty()
    att3_name = db.StringProperty()

  # -
    att1_file = db.BlobProperty()
    att2_file = db.BlobProperty()
    att3_file = db.BlobProperty()

class Add_Confinfo_db(webapp2.RequestHandler):
    def post(self):
        date_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        data_id = date_time + '_' + str(randint(0,1000))
        item = Confinfo_db(key_name=data_id)
        item.data_id = data_id 

        if users.is_current_user_admin():

            item.user_id = users.get_current_user()

        item.year = self.request.get('year')
        item.datetime = self.request.get('datetime')
        item.location = self.request.get('location')
        item.theme = self.request.get('theme')
        item.organizer = self.request.get('organizer')

        if self.request.get('att1_name') and self.request.get('att1_file'):
            item.att1_name = self.request.get('att1_name')
            item.att1_file = self.request.get('att1_file')

        if self.request.get('att2_name') and self.request.get('att2_file'): 
            item.att2_name = self.request.get('att2_name')     
            item.att2_file = self.request.get('att2_file')

        if self.request.get('att3_name') and self.request.get('att3_file'): 
            item.att3_name = self.request.get('att3_name')
            item.att3_file = self.request.get('att3_file')

        item.put()
        time.sleep(1)
        self.redirect('/manage/conference_data')

# Photos related code

class Photo_db(ndb.Model):

    user_id = ndb.UserProperty()
    data_id = ndb.StringProperty()
    year = ndb.StringProperty()
    event_type = ndb.StringProperty()
    catagory = ndb.StringProperty()
  # -
    image_data = ndb.BlobProperty()

    @classmethod
    def _get_catagory(self):
        q = Photo_db.query(projection=[Photo_db.catagory], distinct=True)
        db_data = []
        for result in q.iter():
            db_data.append({'catagory': result.catagory})

        return json.dumps(db_data)

    @classmethod
    def _get_all_catagory_icon(self):

        q = Photo_db.query(projection=[Photo_db.catagory], distinct=True)
        db_data = []
        for result in q.iter():
            q_sub = Photo_db.query(Photo_db.catagory  == result.catagory).get()
            # print "result:", q_sub.data_id, result.catagory
            db_data.append({'data_id': q_sub.data_id, 'catagory': result.catagory})

        return json.dumps(db_data)

    @classmethod
    def _get_catagory_photo(self, catagory):
        q = Photo_db.query(Photo_db.catagory == catagory).fetch(keys_only=True)
        db_data   =[]
        for result in q:
            # print 'lala:',result.data_id, result.catagory
            db_data.append({'data_id':result.string_id()}) 
        # print db_data
        return json.dumps(db_data)

    @classmethod
    def _get_all_photo(self):
        q  = ndb.gql("SELECT data_id,catagory FROM Photo_db")
        db_data   =[]
        for result in q:
            # print 'lala:',result.data_id, result.catagory
            db_data.append({'data_id':result.data_id, 'catagory': result.catagory}) 
        # print db_data    
        return json.dumps(db_data)


class Add_Photo_db(webapp2.RequestHandler):
    def post(self):
        if users.is_current_user_admin():

            for file_data in self.request.POST.getall('photo_file'):
                  #print "File Contents : ", file_data.value
                user = users.get_current_user()
                date_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                data_id = date_time + '_' + str(randint(0,1000))

                item = Photo_db(id=data_id)
                item.data_id = data_id
       
                item.user_id = users.get_current_user()
                item.year = self.request.get('year')
                item.event_type = self.request.get('event_type')
                item.catagory = item.year + '_' + item.event_type
                # print 'lala:', item.catagory
      # -
                photo_file = file_data.value
                if photo_file:
                    photo = images.Image(image_data=photo_file)
                    if photo.width > photo.height:
                        item.image_data = db.Blob(images.resize(photo_file, 800))
                        item.flag = 'horizontal'
                    else:
                        item.image_data = db.Blob(images.resize(photo_file, 600))
                        item.flag = 'vertical'
           #
                item.put()
                time.sleep(1)
                self.redirect('/manage/photo_data')

# load and delete data based on the data type
class loadData(webapp2.RequestHandler):
    def get(self):
        page_address = self.request.uri
        base = os.path.basename(page_address)

        split_address = base.split('?')
        data_set = split_address[1]
        
      
        if data_set == 'registration_data':
            self.response.headers['Content-Type'] = 'application/json'
            self.response.out.write(ConfForm_db._get_registration_data())


        elif data_set == 'job_data':
            db_data = db.Query(Job_db, projection=('data_id', 'job_info', 'post_date'))

        elif data_set == 'conf_data':
            db_data = db.Query(Confinfo_db, projection=('data_id', 'year', 'datetime', 'location', 'theme', 'organizer', 'att1_name', 'att2_name', 'att3_name'))
            db_data.order("-year")
          
        elif data_set == 'photo_data':
            if len(split_address) == 2:
                self.response.headers['Content-Type'] = 'application/json'
                self.response.out.write(Photo_db._get_all_photo())

            elif len(split_address) == 3:
                catagory = split_address[2]
                self.response.headers['Content-Type'] = 'application/json'
                self.response.out.write(Photo_db._get_catagory_photo(catagory))

        elif data_set == 'catagory_icon':
            self.response.headers['Content-Type'] = 'application/json'
            self.response.out.write(Photo_db._get_all_catagory_icon())

        elif data_set == 'catagory_data':
            self.response.headers['Content-Type'] = 'application/json'
            self.response.out.write(Photo_db._get_catagory()) 

        elif data_set == 'abs_data':
            self.response.headers['Content-Type'] = 'application/json'
            self.response.out.write(Abs_db.get_data())


        # -pass to front end        
        data = []
        if data_set == 'job_data' or data_set == 'conf_data':
            for f in db_data:
                data.append(db.to_dict(f))
            print data

            self.response.headers['Content-Type'] = 'application/json'
            self.response.out.write(json.dumps(data))


class deleteData(webapp2.RequestHandler):
    def get(self):
        page_address = self.request.uri
        base = os.path.basename(page_address)

        data_set = base.split('?')[1]
        data_id = base.split('?')[2]

        if users.is_current_user_admin():

            if data_set == "registration_data":
                if data_id == 'all':
                    entries = ConfForm_db.query(keys_only=True)
                    #db.delete(entries)
                    ndb.delete_multi(entries)
                    self.redirect('/manage/load_data?registration_data')
                else:
                    item = ConfForm_db.query(ConfForm_db.data_id == data_id).get()
                    item.key.delete()
                    time.sleep(1)
                    self.redirect('/manage/load_data?registration_data')

            if data_set == "job_data":
                    item = db.Query(Job_db).filter('data_id =', data_id).get()
                    item.delete()
                    time.sleep(1)
                    self.redirect('/manage/load_data?job_data')

            if data_set == "conf_data":
                    item = db.Query(Confinfo_db).filter('data_id =', data_id).get()
                    item.delete()
                    time.sleep(1)
                    self.redirect('/manage/load_data?conf_data')

            if data_set == "photo_data":
                    item = Photo_db.query(Photo_db.data_id == data_id).get()
                    item.key.delete()
                    time.sleep(1)
                    self.redirect('/manage/load_data?photo_data')

            if data_set == "abs_data":
                    user_id = base.split('?')[2] 
                    item = db.Query(Abs_db).filter('user_id =', user_id).get()
                    item.delete()
                    time.sleep(1)
                    self.redirect('/manage/load_data?abs_data')

        if users.get_current_user():
            if data_set == "abs_data":
                user_id = base.split('?')[2] 
                if users.get_current_user().user_id() ==  user_id:
                    item = db.Query(Abs_db).filter('user_id =', user_id).get()
                    item.delete()
                    time.sleep(1)
                    self.redirect('/manage/load_data?abs_data')

class Render_img(webapp2.RequestHandler):
    def get(self):
        page_address = self.request.uri
        base = os.path.basename(page_address)
        data_set = base.split('?')[1]

        if data_set == 'icon':
            data_id = base.split('?')[2]
            item = Photo_db.query(Photo_db.data_id  == data_id).get()
            img = images.Image(item.image_data)
            img.resize(width=120)
            image = img.execute_transforms(output_encoding=images.JPEG)
            self.response.headers['Content-Type'] = 'image/jpeg'
            self.response.out.write(image)

        elif data_set == 'photo':
            set_type = base.split('?')[2]
            data_id = base.split('?')[3]

            item = Photo_db.query(Photo_db.data_id == data_id).get()
            img = images.Image(item.image_data)
            if set_type == 'thumb':
                img.resize(width=60)
            if set_type == 'small':
                img.resize(width=80)
            if set_type == 'medium':
                img.resize(width=250)
            if set_type == 'large':
                img.resize(width=700)
            image = img.execute_transforms(output_encoding=images.JPEG)
            self.response.headers['Content-Type'] = 'image/jpeg'
            self.response.out.write(image)
        else:
            self.response.out.write("No image")

class Render_pdf(webapp2.RequestHandler):
    def get(self):
        page_address = self.request.uri
        base = os.path.basename(page_address)

        split_address = base.split('?')

        data_set = split_address[1]
        data_id = split_address[2]

        if data_set == 'abs_data':
            print "abs"
            user_id = split_address[2]
            print user_id
            item = db.Query(Abs_db).filter('user_id =', user_id).get()
            self.response.headers['Content-Type'] = 'application/pdf'
            self.response.write(item.abs_file)

        if data_set == 'job_data':
            item = db.Query(Job_db).filter('data_id =', data_id).get()
            self.response.headers['Content-Type'] = 'application/pdf'
            self.response.write(item.job_info_file)

        if data_set == 'conf_data':
            att_num = split_address[3]
            item = db.Query(Confinfo_db).filter('data_id =', data_id).get()

            if att_num == '1':
                self.response.headers['Content-Type'] = 'application/pdf'
                self.response.write(item.att1_file)
            if att_num == '2':
                self.response.headers['Content-Type'] = 'application/pdf'
                self.response.write(item.att2_file)
            if att_num == '3':
                self.response.headers['Content-Type'] = 'application/pdf'
                self.response.write(item.att3_file)

class Recieve_comment(webapp2.RequestHandler):
    def post(self):
        #- get comments data
        date_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        data_id = date_time 

        name = self.request.get('name')
        email = self.request.get('email')
        comments = self.request.get('comments')

        #- send confirmation email
        message = mail.EmailMessage(sender="GLCACS <gxfc1616@gmail.com>",
                            subject="New Comments Recieved")

        message.to = "gxfc1616@gmail.com"
        message.body = 'Recieved Time: ' + data_id + '\n' + 'Name: ' + name + '\n' + 'Email: ' + email + '\n' + 'comments: ' + comments + '\n'  
    

        message.send()     

        self.redirect("/contact/thankyou");  

class Layout_db(db.Model):
    data_type = db.StringProperty()
    html_code = db.TextProperty()
        
class Save_edit_changes(webapp2.RequestHandler):
    def post(self):
        user = users.get_current_user()
        page_address = self.request.uri
        base = os.path.basename(page_address)
        split_address = base.split('?')
        data_type = split_address[1]

        if users.is_current_user_admin():
            item = Layout_db.get_by_key_name(data_type)

            if item:
                html_code = self.request.get('html_code')
                if data_type == 'conference_registration':
                    item.html_code = html_code.split('<!--separation-->')[0] + tp.conf_registration_form_html + html_code.split('<!--separation-->')[1] + tp.submit_abs_link_html
                else:
                    item.html_code = html_code
            else:
                item = Layout_db(key_name=data_type)
                item.data_type = data_type
                html_code = self.request.get('html_code')
                if data_type == 'conference_registration':
                    item.html_code = html_code.split('<!--separation-->')[0] + tp.conf_registration_form_html + html_code.split('<!--separation-->')[1] + tp.submit_abs_link_html
                else:
                    item.html_code = html_code

            #print 'lala:',item.html_code

            item.put()
            time.sleep(1)

            if data_type == 'conference_registration':
                self.redirect('/conference_registration')
            else:
                self.redirect('/')

class Get_layout(webapp2.RequestHandler):
    def get(self):
        page_address = self.request.uri
        base = os.path.basename(page_address)
        data_type = base.split('?')[1]

        if data_type == 'event':
            q = Layout_db.get_by_key_name('event')
        else:
            q = Layout_db.get_by_key_name('conference_registration')

        db_data = {}
        db_data ={'data_type': q.data_type, 'html_code': q.html_code}

        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(db_data))



app = webapp2.WSGIApplication([
    ('/?', Routes_handler),
    ('/about_us/?', Routes_handler),
    ('/conference/?', Routes_handler),

    ('/conference_registration/?', Routes_handler),
      ('/conference_registration/add_record/?', Add_ConfForm_db),  
      ('/conference_registration/csv/?', Create_csv),
      ('/conference_registration/thankyou?', Routes_handler),  
      ('/conference_registration/check_registration?', Routes_handler),
      ('/conference_registration/find_registration?', Find_registration), 
      ('/conference_registration/submit_form?', Routes_handler),
      ('/conference_registration/submit_abs?', Add_Abs_db), 
      ('/conference_registration/abs_data', Routes_handler),

    ('/activities/?', Routes_handler),
        ('/activities/([^/]+)/?', Activity_photo_page),
    ('/jobs/?', Routes_handler),
      
    ('/contact/?', Routes_handler),
      ('/contact/recieve_comment/?', Recieve_comment),  
      ('/contact/thankyou/?', Routes_handler),
    # 
    ('/manage/?', Routes_handler), 

    ('/manage/registration_data/?', Routes_handler),
    ('/manage/job_data/?', Routes_handler),
    ('/manage/conference_data/?', Routes_handler),
    ('/manage/photo_data/?', Routes_handler),

    ('/manage/publish_photo/?', Routes_handler), 
    ('/manage/publish_icon/?', Routes_handler), 
    ('/manage/publish_job/?', Routes_handler), 
    ('/manage/publish_conference/?', Routes_handler), 

    ('/manage/add_job/?', Add_Job_db),
    ('/manage/add_conf/?', Add_Confinfo_db),
    ('/manage/add_photo/?', Add_Photo_db),

    ('/manage/load_data/?', loadData),
    ('/conference_registration/load_data?', loadData),
    ('/delete_data/?', deleteData),

    ('/manage/render_img/?', Render_img), # - photo
    ('/manage/render_pdf/?', Render_pdf), # - pdf
    ('/conference_registration/render_pdf/?', Render_pdf),

    ('/manage/modify_event/?', Routes_handler), 
    ('/manage/modify_conference/?', Routes_handler),

    ('/manage/save_edit_changes/?', Save_edit_changes), 
    ('/manage/get_layout/?', Get_layout),     

], debug=True)