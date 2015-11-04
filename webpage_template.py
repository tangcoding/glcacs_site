
# navigation bar

public_navbar_html = '''
<style>..navbar-nav{margin: 0 auto;}</style>
  <nav class="top_navbar navbar-default">
    <div class="container-fluid">
        <h2>Chinese American Chemical Society - the Great Lakes Chapter</h2>
    </div> <!--.container-fluid-->
  </nav><!--.top_navbar-->

  <nav class="main_navbar navbar-inverse">
    <div class="container-fluid">

        <div class="navbar-header">  
          <button class="navbar-toggle" type="button" data-toggle="collapse" data-target="#public_Navbar">   
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>                        
          </button> <!--.navbar-toggle-->
          <a class="navbar-brand" href="/">GLCACS</a>
        </div> <!-- .navbar-header -->

        <div class="collapse navbar-collapse" id="public_Navbar">
          <ul class="nav navbar-nav">
            <li><a href="/">Home</a></li>
            <li><a href="/about_us">About Us</a></li>
            <li><a href="/conference">Conference</a></li>
            <li><a href="/conference_registration">Registraion</a></li>
            <li><a href="/activities">Activities</a></li>
            <li><a href="/jobs">Sponsors&Jobs</a></li>
            <li><a href="/contact">Contact</a></li>
          </ul>
        </div> <!--.collapse-->
    </div> <!--.container-fluid-->
  </nav>
'''

manage_navbar_html = '''

<nav class="navbar-default">
    <div class="container-fluid">

        <div class="navbar-header">  
          <button class="navbar-toggle" type="button" data-toggle="collapse" data-target="#admin_Navbar">   
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>                        
          </button> <!--.navbar-toggle-->
          <a class="navbar-brand" href="/">GLCACS</a>
        </div> <!-- .navbar-header -->

        <div class="collapse navbar-collapse" id="admin_Navbar">  
          <ul class="nav navbar-nav manage_nav">

            <li><a href="/">Public &nbsp;&nbsp;|</a></li>

            <li class="dropdown">
              <a class="dropdown-toggle" data-toggle="dropdown" href="#">
                Manage Data <span class="caret"></span>
              </a>
              <ul class="dropdown-menu">
                <li><a href="/manage/registration_data">Registration Data</a></li>
                <li><a href="/manage/job_data">Job Data</a></li>
                <li><a href="/manage/conference_data">Conference Data</a></li>
                <li><a href="/manage/photo_data">Photos Data</a></li>
              </ul>
          </li> <!--.dropdown-->

          <li class="dropdown">
              <a class="dropdown-toggle" data-toggle="dropdown" href="#">
                Modify Webpage <span class="caret"></span>
              </a>
              <ul class="dropdown-menu">
                <li><a href="/manage/modify_event">Upcoming Event</a></li>
                <li><a href="/manage/modify_conference">Registration Page</a></li>
              </ul>
          </li> <!--.dropdown-->
        </ul>
      </div> 

    </div> <!--.container-fluid-->
  </nav>
  '''

# admin 

# - main manage page
login_page_html = '''

'''

# -publish photo page

publish_photo_page_html = '''

<div class=".main_container">
  <form name="add_photo_form" method="post" action="/manage/add_photo" enctype="multipart/form-data">
          <h3>Publish Photo</h3> 

          <div class="form-group">
            <label>Year*</label>
            <input class="form-control" type="text" name="year" placeholder="YYYY" required>
          </div><!-- .form-group -->

          <div class="form-group">
            <label>Event Type*</label>
            <select name="event_type" required>
                <option value="" selected> -- Select an Catagory -- </option>
                <option value="conference">Conference</option>
                <option value="picnic">Picnic</option>
            </select>
          </div><!-- .form-group -->

          <div class="form-group">
            <a class="btn btn-default" onclick="$('input[name=photo_file]').click();">Attachd Photo File(s)*</a>
            <input type="file" name="photo_file" multiple required>
            <span id="photo_file_path"></span>
          </div><!-- .form-group -->

          <input type="submit" class="btn btn-default" name="submit" value="Add">
          <input type="reset" class="btn btn-default" value="Reset">
  </form>

</div> <!-- .main_container -->
'''


# -publish job page

publish_job_page_html = '''

<div class=".main_container">
  <form name="add_job_form" method="post" action="/manage/add_job/" enctype="multipart/form-data">
          <h3>Publish Job Info</h3> 

          <div class="form-group">
            <label>Job Description*</label>
            <textarea class="form-control" name="job_info" maxlength="1000"  rows="3" placeholder="e.g. Principal Scientist -- Green Chemistry" required></textarea>
          </div><!-- .form-group -->

          <div class="form-group">
            <a class="btn btn-default" onclick="$('input[name=job_info_file]').click();">Attachd Job Info File*</a>
            <input type="file" name="job_info_file" required>
            <span id="job_file_path"></span>
          </div><!-- .form-group -->


          <div class="form-group">
            <label>Post Date*</label>
            <input class="form-control" type="date" name="post_date" placeholder="YYYY-MM-DD" required>
          </div><!-- .form-group -->

          <input type="submit" class="btn btn-default" name="submit" value="Add">
          <input type="reset" class="btn btn-default" value="Reset">
  </form>

</div> <!-- .main_container -->
'''

# -publish conference info page
publish_conference_page_html = '''

<style>
</style>

<div class=".main_container">
  <form name="add_conf_form" method="post" action="/manage/add_conf/" enctype="multipart/form-data">
          <h3>Add New Conference Information</h3> 

          <div class="form-group">
            <label>Year*</label>
            <input class="form-control" type="text" name="year" placeholder="YYYY" required>
          </div><!-- .form-group -->

          <div class="form-group">
            <label>Date and Time*</label>
            <input class="form-control" type="text" name="datetime" placeholder="e.g. Saturday, May 2, 2015, 8:40 AM - 6:00 PM " required>
          </div><!-- .form-group -->

          <div class="form-group">
            <label>Location*</label>
            <input class="form-control" type="text" name="location" placeholder="e.g. Abbott Laboratories, 200 Abbott Park Road, Abbott Park, IL 60064, USA" required>
          </div><!-- .form-group -->

          <div class="form-group">
            <label>Theme*</label>
            <input class="form-control" type="text" name="theme" placeholder="e.g. Career Development for Chemists and Chemical Engineers" required>
          </div><!-- .form-group -->

          <div class="form-group">
            <label>Organizer*</label>
            <input class="form-control" type="text" name="organizer" placeholder="e.g. Great Lakes Chapter (GLCACS)" required>
          </div><!-- .form-group -->

          <hr>

          <div class="form-group">
            <label>Attachment 1</label>
            <input class="form-control" type="text" name="att1_name" placeholder="File Description e.g. Conference Brochure">

            <a class="btn btn-default" onclick="$('input[name=att1_file]').click();">Add File</a>
            <input type="file" name="att1_file">
            <span id="att1_file_path"></span>
          </div><!-- .form-group -->

          <div class="form-group">
            <label>Attachment 2</label>
            <input class="form-control" type="text" name="att2_name" placeholder="File Description e.g. Presentation Winners">

            <a class="btn btn-default" onclick="$('input[name=att2_file]').click();">Add File</a>
            <input type="file" name="att2_file">
            <span id="att2_file_path"></span>
          </div><!-- .form-group -->

          <div class="form-group">
            <label>Attachment 3</label>
            <input class="form-control" type="text" name="att3_name" placeholder="File Description e.g. Driving Direction">

            <a class="btn btn-default" onclick="$('input[name=att3_file]').click();">Add File</a>
            <input type="file" name="att3_file">
            <span id="att3_file_path"></span>
          </div><!-- .form-group -->
         
          <input type="submit" class="btn btn-default" name="submit" value="Add">
          <input type="reset" class="btn btn-default" value="Reset">
  </form>

</div> <!-- .main_container -->

'''

# -view registration data page
registration_data_page_html = '''

<div class="main_container">

  <button class="btn btn-default" ng-click='delete_all()'>Delete All Data</button>
  <a href="/conference_registration/csv/" target="_blank" class="btn btn-default">Export CSV File</a>

  <div class="table-responsive">
    <table class="table data_table">
      <tr>
        <td> Add Date </td>
        <td> Name </td>
        <td> Email </td>
        <td> Affiliation </td>
        <td> Comments </td>
        <td> Delete</td>
      </tr>

      <tr ng-repeat="item in reg_data ">
        <td> [! item.data_id | limitTo: 8 !] </td>
        <td> [! item.name !] </td>
        <td> [! item.email !] </td>
        <td> [! item.affiliation !] </td>
        <td> [! item.comments !] </td>
        <td class="del_mark" ng-click="delete(item.data_id)"> <span class="glyphicon glyphicon-remove"></span></td>    
      </tr>
    </table>
  </div> <!--.table-responsive-->
</div> <!--.main_container-->
'''


# -view job data page
job_data_page_html = '''

  <div class="main_container">
    <a href="/manage/publish_job" class="btn btn-default">
          Add a New Job
    </a>

    <a href="/manage/load_data?job_data" class="btn btn-default">json</a>
    <table class="table data_table">
      <tr>
        <td> Job Description </td>
        <td> Post Date </td>
        <td> Attached File </td>
        <td> Delete </td>
      </tr>

      <tr ng-repeat="item in job_data  ">
        <td> [! item.job_info !] </td>
        <td> [! item.post_date !] </td>
        <td><a ng-href="/manage/render_pdf?job_data?[!item.data_id!]">Click to See</a></td>
        <td class="del_mark" ng-click="delete(item.data_id)"> <span class="glyphicon glyphicon-remove"></span></td>    
      </tr>
    </table>

    
  </div> <!--.main_container-->
'''

# -view conference data page
conference_data_page_html = '''

  <style>
    td ul {list-style-type: none; padding-left:0;}
    td ul li a{text-decoration: underline; color: blue;}
    input['.select_year']{border-radius: 10px; height: 0.95rem;}
  </style>

  <div class="main_container">
    

    <a href="/manage/publish_conference" class="btn btn-default">
      Add a New Conference Info
    </a>
    <a href="/manage/load_data?conf_data" class="btn btn-default">json</a>
    <hr>

    <div class="input-group">
      <span class="input-group-addon" id="basic-addon1">Only show the Year of:</span>
      <input ng-model='select_year' type="text" class="form-control" placeholder="YYYY" aria-describedby="basic-addon1">
    </div>

    <table class="table data_table">
      <tr>
        <td> Year </td>
        <td> Date </td>
        <td> Location </td>
        <td> Theme </td>
        <td> Organizer </td>
        <td> Attachment </td>
        <td> Delete </td>
      </tr>

      <tr ng-repeat="item in conf_data | filter:select_year:true ">
        <td> [! item.year !] </td>
        <td> [! item.datetime !] </td>
        <td> [! item.location !] </td>
        <td> [! item.theme !] </td>
        <td> [! item.organizer !] </td>
        <td> 
          <ul>
            <li>
              <a ng-href="/manage/render_pdf?conf_data?[!item.data_id!]?1">
                [! item.att1_name !]
              </a>
            </li>
            <hr>

            <li>
              <a ng-href="/manage/render_pdf?conf_data?[!item.data_id!]?2">
                [! item.att2_name !]
              </a>
            </li>
            <hr>

            <li>
              <a ng-href="/manage/render_pdf?conf_data?[!item.data_id!]?3">
                [! item.att3_name !]
              </a>
            </li>
          </ul>
        </td>

        <td class="del_mark" ng-click="delete(item.data_id)"> 
          <span class="glyphicon glyphicon-remove"></span>
        </td>    
      </tr>
    </table>

    
  </div> <!--.main_container-->
'''

# -view photos data page
photo_data_page_html = '''


<div class="main_container text_left">
  <a href="/manage/publish_photo" class="btn btn-default">
    Add Photos
  </a>

  <a href="/manage/load_data?photo_data" class="btn btn-default">json</a>
  <hr>
 
 
  <label>Select the Catagory to Show Photos: &nbsp;</label>
 <div class="input-group">
  <select ng-model="selected">
      <option ng-repeat="item in catagory_list" value="[! item.catagory!]">[! item.catagory!]</option>
  </select>
    </div><!--.input-group-->  

  <table class="table data_table">
    <tr>
      <td> Catagory</td>
      <td> Preview </td> 
      <td> Delete </td>
    </tr>

    <tr ng-repeat="item in photo_data | filter:{catagory:selected} :true">
      <td> [! item.catagory !] </td>
      <td><img ng-src="/manage/render_img?photo?thumb?[!item.data_id!]"></td> 

      <td class="del_mark" ng-click="delete(item.data_id)"> 
        <span class="glyphicon glyphicon-remove"></span>
      </td>    
    </tr>
  </table>
</div> <!--.main_container-->
'''

# modify event page 
modify_event_page_html = '''

<style type="text/css" media="screen"> 
    form {margin: 0 auto; text-align: center; background: #fff; width: 80%;}
    #editor { width: 100%; height: 70%; min-height:300px; max-height: 500px; margin: 0 25px 25px 25px; text-align: left;}
    #event_html { width: 70%; height: 58px; opacity: 1; margin: 0 auto;}
</style>

 <div class="main_container">
  <form action="/manage/save_event_changes" method="post">
    <textarea id="event_html" name='html_code'>[!event_template!]</textarea>
    <div id="editor">
    </div>

    <input class="btn btn-default" type="submit" value="Save Changes">
  </form>
  

  <script src="/files/ace.js" type="text/javascript" charset="utf-8"></script>
  <script>
      var editor = ace.edit("editor");
      editor.setTheme("ace/theme/dawn");
      editor.getSession().setMode("ace/mode/html");
      //editor.getSession().setUseWrapMode(true);

      editor.getSession().setValue($('#event_html').val());
      console.log($('#event_html').val());
      editor.getSession().on('change', function(){
        $('#event_html').val(editor.getSession().getValue());
        
      });
  </script>
</div> <!--.main_container-->
'''

# -public pages

# Carousel item

carousel_lg = '''
          <div class="item">
            <img src="/images/bg2.jpg" alt="Annual_Meeting" width="100%">
            <div class="carousel-caption">
              <h2>Chinese American Chemical Society
                  <br>
                  - the Great Lakes Chapter</h2>
            </div> <!--.carousel-caption-->
          </div><!--.item-->
        
          <div class="item">
            <img src="/images/bg3.jpg" alt="Annual_Meeting" width="100%">
            <div class="carousel-caption">
              <h2>Chinese American Chemical Society
                  <br>
                  - the Great Lakes Chapter</h2>
            </div> <!--.carousel-caption-->
          </div><!--.item-->

        <!-- Indicators -->
        <ol class="carousel-indicators">
          <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
          <li data-target="#myCarousel" data-slide-to="1"></li>
          <li data-target="#myCarousel" data-slide-to="2"></li>
        </ol>
'''
carousel_lg="".join(carousel_lg.split('\n'))


# home page
home_page_html = '''
    <style>
        #hidden_text{ display:none;}
        .collapse_text, .glyphicon-collapse-down, .glyphicon-collapse-up{color:#0097A7;}
    </style> 

    <div class="main_container">

      <div id="myCarousel" class="carousel slide" data-ride="carousel">
       
        <!-- Wrapper for slides -->
        <div class="carousel-inner" role="listbox">
          <div class="item active">
            <img src="/images/bg1.jpg" alt="Chicago" width="100%">
            <div class="carousel-caption">
              <p>Chinese American Chemical Society --the Great Lakes Chapter</p>
            </div> <!--.carousel-caption-->
          </div><!--.item-->

          <div class="item">
            <img src="/images/bg2.jpg" alt="Annual_Meeting" width="100%">
            <div class="carousel-caption">
              <p>Promote Fellowship Among Chinese American Chemists and Chemical Engineers</p>
            </div> <!--.carousel-caption-->
          </div><!--.item-->
        
          <div class="item">
            <img src="/images/bg3.jpg" alt="Annual_Meeting" width="100%">
            <div class="carousel-caption">
              <p>Enhance Communication and Professional Interaction Among Members</p>
            </div> <!--.carousel-caption-->
          </div><!--.item-->

          <div class="item">
            <img src="/images/bg4.jpg" alt="Annual_Meeting" width="100%">
            <div class="carousel-caption">
              <p>Provide A Network for Mutual Professional Enhancement and Career Development</p>
            </div> <!--.carousel-caption-->
          </div><!--.item-->

        <!-- Indicators -->
        <ol class="carousel-indicators">
          <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
          <li data-target="#myCarousel" data-slide-to="1"></li>
          <li data-target="#myCarousel" data-slide-to="2"></li>
          <li data-target="#myCarousel" data-slide-to="3"></li>
        </ol>
          

        </div><!--.carousel-inner-->
     
      </div><!--.carousel-->
   
      <div class="intro text_justify">
        <h3>GLCACS</h3>
        <p>
          GLCACS is the local chapter of Chinese American Chemical Society (CACS) in the Great Lakes area, including Illinois, Indiana, Wisconsin, Michigan, Minnesota, and Ohio. CACS is the only Chinese-American professional organization that is officially recognized by both American Chemical Society (ACS) and the American Institute of Chemical Engineers (AIChE). 
            <span class="collapse_text">More</span>&nbsp;<span class="glyphicon glyphicon-collapse-down"></span> 
          </p>

          <p id="hidden_text">
            Since its founding, GLCACS has played an active role in promoting professional development and networking for GLCACS members and non-members alike. Our members are comprised of professionals from Midwest industry as well as professors, research fellows, and students in Midwest universities. 

           Each year, usually in May, GLCACS holds its annual conference in Chicago region. The conference invites senior executives from industry and professors from universities to give plenary speeches. The conference provides GLCACS members and non-members a great opportunity to discuss cutting-edge R&D in both industrial and academic research, focusing on but not limited to chemical, pharmaceutical, food, energy, biotechnological areas. It also serves as a platform for exchanging information, connecting people, and exploring career development. Our conference provides free registration, free lunch, free parking, and subsidized dinner. Come join us in every May and share your thoughts with your peers. 

           GLCACS also organizes a summer picnic in Chicago region in August, which is another great networking opportunity for both working professionals and students. The picnic offers a variety of food, which include catered food from local Chinese restaurant, BBQ, fruits, and drinks. It also provides games to both adults and children. Come join us in each August to enjoy the last piece of summer in Midwest.
          </p> <!-- #hidden_text -->

      </div> <!-- #hidden_text -->


      <div class="event " ng-bind-html="html_code">
<!--          <h3><span class="glyphicon glyphicon-calendar"></span> Upcoming Event</h3>
        <h4>CACS Banquet at ACS 2015 National Meeting in Boston</h4>
        <ul class="text_left">
          <li>Date: Aug 17, 2015 5:30 PM - 9:30 PM</li>
          <li>Location: <br>
            Hei La Moon Restaurant <br>
            88 Beach Street, <br>
            Boston, MA 02111</li>
        </ul> -->
-->
      </div><!--.event-->

      <div class="other">
        <h3>Looking for a Job?</h3>
        <p>We post job openings here!<p>

        <h3>Related Link</h3>
        <p>Chinese American Chemical Society (CACS)<p>  
      </div><!--.other-->
   </div> <!--.main_container-->
'''

# about us page
about_us_page_html = '''

  <div class="main_container text_justify">
        <h3>Who We Are and Our Mission</h3>
        <p>
        GLCACS is a Chapter of Chinese American Chemistry Society (CACS). CACS is a non-profit professional organization and does not have political affiliation of regional or national bias. GLCACS covers Midwest states that include Illinois, Indiana, Iowa, Minnesota, Michigan, Ohio, and Wisconsin. GLCACS Objectives are:
        </p>
        <ul>
            <li>To promote fellowship among Chinese American chemists, chemical engineers, and those working in related scientific areas.</li>
            <li>To enhance communication and professional interaction among its members.</li>
            <li>To provide a forum for the discussion of issues of mutual interest and concerns.</li>
            <li> To create opportunities for its members to share professional experiences and to participate in joint research and business ventures.</li>
            <li>To provide a network for mutual professional enhancement and career development.</li>
            <li>To provide career counseling for the young people, particularly those interested in the scientific and engineering careers.</li>
            <li>To encourage scholarly achievements in chemistry and chemical engineering, and to recognize individuals who have made outstanding contributions to the science and technology of chemistry and chemical engineering.</li>
            <li>To facilitate interactions between CACS and other scientific organizations and communities.
            </li>
        </ul>
        <br>
        <h3>Current Committee</h3>
        <ul class="committee">
            <li><b>President:</b> Wei Zhang (Abbott)</li>
            <li><b>Chair:</b> Elyse Zhang (NL Chemical)</li>
            <li><b>Co-chair:</b> Dongxu Shu (Northwestern Univ.)</li>
            <li><b>Scientific Directors:</b> Lubo Zhou (UOP LLC), Robin Wang (NL Chemical), Xiaomao Wu (Abbott)</li>
            <li><b>University and Student Section Directors:</b> Stephanie Li (UOP LLC), Lixiao Zeng (UOP LLC), Jiazhen Chen (Northwestern Univ.)</li>
            <li><b>Treasurer:</b> Yanqun Zhao (AbbVie Inc.)</li>
            <li><b>Webmaster:</b> Wenjie Tang (UMN), Lijun Xu (UOP LLC)</li>            
        </ul> 
  </div> <!--.main_container-->

'''

# conference page
conference_page_html = '''
<style type="text/css">
  .conf_data a {color:blue; text-decoration: underline;}
</style>

<div class="main_container">
  <div class="conf_data text_left" ng-repeat="item in conf_data">

      <h3>[! item.year !] Conference</h3>
      <p>
          The [! item.year - 1996 !]th Annual Conference of the Chinese American Chemical Society 
          <br>[! item.organizer !]
          <br><br>
          Conference Theme: <b> [! item.theme !]</b>
          <br>
          Date: [! item.datetime !]
          <br><br>
          Location: <i>[! item.location !] </i>
          <br><br>
          
          <a ng-href="/manage/render_pdf?conf_data?[!item.data_id!]?1">
              [! item.att1_name !]
          </a>
          &nbsp; &nbsp;
          <a ng-href="/manage/render_pdf?conf_data?[!item.data_id!]?2">
              [! item.att2_name !]
          </a>
          &nbsp; &nbsp;
          <a ng-href="/manage/render_pdf?conf_data?[!item.data_id!]?3">
              [! item.att3_name !]
          </a>

       </p>
       <hr>
  <div>

</div> <!--.main_container -->
'''

# activity page
activities_page_html = '''
<style>
  .conf_pic, .picnic_pic{width: 100%; text-align: left; margin: 35px auto;}
  .img_icon{ display: inline-block; margin: 0 15px; text-align: center;}
  .img_icon img {height: 80px;}
</style>

<div class="main_container">
  <div class="conf_pic">
    <h3>Conference</h3>
    <div ng-repeat="item in catagory_icon | filter: {catagory: 'conference'} | orderBy: '-catagory'"  class="img_icon">
      <a ng-href="/activities/[! item.catagory!]">
        <p>[! item.catagory | limitTo:4 !]</p>
        <img ng-src="/manage/render_img?icon?[!item.data_id!]">
      </a>
    </div>
  </div><!--.conf_pic-->

  <div class="picnic_pic">
    <h3>Picnic</h3>
    <div ng-repeat="item in catagory_icon | filter: {catagory: 'picnic'} | orderBy: '-catagory'" class="img_icon">
      <a ng-href="/activities/[!item.catagory!]">
        <p>[! item.catagory | limitTo:4 !]</p>
        <img ng-src="/manage/render_img?icon?[!item.data_id!]">
      </a>
    </div>      
  </div><!--.picnic_pic--> 
<div><!--.main_container-->
'''

# activity photos page
activity_photos_page_html = '''
  <style>
    .image_wrap{width: 675px; height: 400px; text-align: center; margin: 25px auto;}
    .image_wrap img { height: 100%; }
    .thumb_wrap{width: 100%; text-align: left; margin: 25px auto; padding: 0 15px;}
    .photo_thumb { display: inline-block; height: 50px; margin-right: 10px; cursor: pointer; }
    .photo_thumb img { height: 50px; opacity: 0.8; transition: all 0.5s ease;  }
    .photo_thumb img:hover { opacity: 1; transition: all 0.5s ease; }
  </style>

  <a class="btn btn-default hide" href="/manage/load_data?photo_data?2015_conference">show jason file</a>

  <div class="main_container">
    <div class="image_wrap">
      <img ng-src="/manage/render_img?photo?large?[!mainImageUrl!]">
    </div><!-- .image_wrap - -->

    <div class="thumb_wrap">
      <div class="photo_thumb" ng-repeat="item in activity_photos" ng-click="setImage(item)"><img ng-src="/manage/render_img?photo?small?[!item.data_id!]" />
      </div><!-- .photo_thumb - -->
    </div><!-- .thumb_wrap - -->
  <div><!--.main_container-->
'''

# conference registration page
conf_registration_page_html = '''
<style>
form { margin: 0 auto; padding: 25px; border-radius: 5px;}
label {width: 100px; text-align:left;}
.main_container a{text-decoration:underline; color:#0097A7;}
.main_container h3{text-decoration:none;}
</style>
<div class="main_container text_justify" ng-bind-html="html_code">

</div> <!--.main_container-->
'''

# thank you page for conference registration
registration_thankyou_page_html = '''
<div class="main_container">
  <div class="alert alert-success" role="alert">
          <b>Thank you for your registration. </b>
          <br> A confirmation email will be sent to you.
  </div> <!-- .alert -->
</div> <!--.main_container-->
'''

# check if user has regisered page
check_registration_page_html = '''
<div class="main_container">
  <form name="check_reg_form" method="post">
      <div class="form-group">
        <label>confirmation Number*</label>
        <input class="form-control" type="text" name="confirmation_num" maxlength="50" ng-model='confirmation_num' required>
      </div><!-- .form-group -->

     <div class="form-group">
        <label>Email*</label>
        <input class="form-control" type="email" name="email" maxlength="50"  ng-model='email' required>
      </div><!-- .form-group -->

      <input ng-disabled='check_reg_form.$invalid' ng-click='find_reg()' type="submit" class="btn btn-default" name="submit" value="Submit">
      <input type="reset" class="btn btn-default" value="Reset">
    </form>

    <div class="alert alert-success" ng-show='show_flag' role="alert">
            <b>[!msg!] </b>
    </div> <!-- .alert -->

</div> <!--.main_container-->
'''

# submit abstract page
submit_abstract_page_html = '''
<div class="main_container">
    <a href="/conference_registration/abs_data" class="btn btn-default">See Abstract Data</a>

  <form name="sub_abs_form" method="post" action="/conference_registration/submit_abs" enctype="multipart/form-data">

      <div class="form-group">
        <label>confirmation Number*</label>
        <input class="form-control" type="text" name="confirmation_num" maxlength="50" ng-model='confirmation_num' required>
      </div><!-- .form-group -->

     <div class="form-group">
        <label>Name*</label>
        <input class="form-control" type="text" name="name" maxlength="50"  ng-model='name' required>
      </div><!-- .form-group -->

      <div class="form-group">
        <a class="btn btn-default" onclick="$('input[name=abs_file]').click();">Attachd PDF File* (less than 1M)</a>
        <input type="file" name="abs_file" required>
        <span id="abs_file_path"></span>
      </div><!-- .form-group -->

      <input ng-disabled='sub_abs_form.$invalid' type="submit" class="btn btn-default" name="submit" value="Submit">
      <input type="reset" class="btn btn-default" value="Reset">
    </form>

    <div class="alert alert-success" ng-show='show_flag' role="alert">
            <b>[!msg!] </b>
    </div> <!-- .alert -->

</div> <!--.main_container-->
'''

# -view abstract data page
abs_data_page_html = '''

<div class="main_container">
    <a href="/conference_registration/submit_form" class="btn btn-default">
          Update Abstract
    </a>

    <a href="/conference_registration/load_data?abs_data" class="btn btn-default">json</a>
    <table class="table data_table">
      <tr>
        <td> Name </td>
        <td> Email</td>
        <td> Confirmation # </td>
        <td> Abstract </td>
        <td> Delete </td>
      </tr>

      <tr ng-repeat="item in abs_data  ">
        <td> [! item.name !] </td>
        <td> [! item.email !] </td>
        <td> [! item.data_id !] </td>
        <td><a ng-href="/conference_registration/render_pdf?abs_data?[!item.user_id!]">Click to See</a></td>
        <td class="del_mark" ng-click="delete(item.user_id)"> <span class="glyphicon glyphicon-remove"></span></td>    
      </tr>
    </table>

</div> <!--.main_container-->
'''
# contact us page
contact_page_html = '''
<div class="main_container">  
  <form name="comments_form" method="post" action="/contact/recieve_comment">
    <div class="form-group">
      <label>Name*</label>
      <input class="form-control" type="text" name="name" maxlength="50" ng-model='name' required>
    </div><!-- .form-group -->

   <div class="form-group">
      <label>Email*</label>
      <input class="form-control" type="email" name="email" maxlength="50"  ng-model='email' required>
    </div><!-- .form-group -->



    <div class="form-group">
      <label>Your Comments* (minimum 20 charaters):</label>

      <textarea class="form-control" name="comments" ng-minlength="20" maxlength="1000"  rows="5" ng-model='comments' required></textarea>
    </div><!-- .form-group -->


    <input ng-disabled='comments_form.$invalid' type="submit" class="btn btn-default" name="submit" value="Submit">
    <input type="reset" class="btn btn-default" value="Reset">
  </form>

        
</div> <!-- .main_container -->
'''

# thank you page for conference registration
contact_thankyou_page_html = '''
<div class="main_container">
  <div class="alert alert-success" role="alert">
    <b>Thank you for submitting your comments. </b>
  </div> <!-- .alert -->
</div> <!--.main_container-->
'''


# sponsors and jobs page
jobs_page_html='''

    <style>
      table tr td {width: 250px; height: 150px; text-align:center;}
      table tr td  img{max-width: 180px; max-height: 150px;}
      .job_date{color:#B71C1C;}
      .job ul li a{text-decoration: underline;}
    </style>

    <div class="main_container text_justify">
      <div class="sponsor">
          <h3 class="text_left">We appreciate the sponsorship from:</h3>
          <table>
              <tr>
                  <td>
                      <a href="http://www.baxter.com" target="_blank">
                          <img src="/images/sponsor_logo/Baxter-Logo.gif"> 
                      </a>
                  </td>
                  <td>
                      <a href="http://www.uop.com" target="_blank">
                          <img src="/images/sponsor_logo/nl.png">
                      </a>
                  </td>
                  <td>
                      <a href="http://www.uop.com" target="_blank">
                          <img src="/images/sponsor_logo/uop_logo.jpg">
                      </a>
                  </td>
              </tr>
              <tr>
                  <td>
                      <a href="http://www.abbott.com" target="_blank">
                          <img style="width:330px;" src="/images/sponsor_logo/abbott.jpg"> 
                      </a>
                  </td>
                   <td>
                      <a href="http://www.spherotech.com/" target="_blank">
                          <img style="width:105px;" src="/images/sponsor_logo/Sphero.jpg">
                      </a>
                  </td>
              </tr>
              <tr>
                  <td>
                      <a href="http://www.abbvie.com" target="_blank">
                          <img src="/images/sponsor_logo/abbvie.jpg"> 
                      </a>
                  </td>
                   <td>
                      <a href="http://www.nicenergy.com" target="_blank">
                          <img src="/images/sponsor_logo/nice_logo.jpg">
                      </a>
                  </td>
                  <td>
                    <a href="http://www.hospira.com" target="_blank">
                          <img src="/images/sponsor_logo/Hospira.jpg">
                      </a>
                   </td>
              </tr>
          </table>
      </div> <!--.sponsor -->

      <div class="hr text_left">
        <h3>HR Links:</h3>
        <ul>
            <li> 
                Abbott Lab ( 
                <a href="https://recruit.smashfly.com/optin.aspx?c=g83QiIHWoK4iwSc0EOGP35V1smdfEb9q">HR link</a>
                &nbsp; or &nbsp;
                <a href="/files/Abbott_QR_code.pdf">QR code</a>
                &nbsp;)
            </li>
        </ul>
      </div> <!--.hr -->
            
      <div class="job text_left">
        <h3>Job Openings:</h3>
        <ul>
          <li ng-repeat="item in job_data ">
            <a ng-href="/manage/render_pdf?job_data?[!item.data_id!]"> 
              [!item.job_info!]
            </a>
            <em><span class="job_date">(posted on [!item.post_date !])</span></em>
          </li>
        </ul>
      </div> <!--.job -->

     </div><!--.main_container-->
'''


event_template_html = '''
<h3><span class="glyphicon glyphicon-calendar"></span> Upcoming Event</h3>
<h4>CACS Banquet at ACS 2015 National Meeting in Boston</h4>
<ul class="text_left">
  <li>Date: Aug 17, 2015 5:30 PM - 9:30 PM</li>
  <li>Location: <br>
    Hei La Moon Restaurant <br>
    88 Beach Street, <br>
    Boston, MA 02111</li>
</ul> 
'''

conf_registration_template_html = '''
<h3>The 19th Annual Conference Registration (2015)</h3>
<p><b>Registration for 2015 Annual Conference is closed.</b></p>
<span>Registration deadline:</span> by April 30, 2015 for online registration. 
<br><br>
<span>Registration steps:</span> please submit the registration form (Step 1), then go to Step 2 if you like to participate in the competition of the presentation.

<!--separation-->

<h4>Step 2. Documents for Presentation Section</h4>
<h4>Documents for Presentation Section</h4>
<p>
<span>Deadline:</span> Please submit the completed form (download from link below) and an extended abstract by <span>April 29th</span> to participate in the presentation competition! Please find the following documents for more detailed requirements for presentation section. A total of 600 dollars will be awarded for the winners. Please send your application form and extended abstract to <a href="mailto:glcacsposter@gmail.com">glcacsposter@gmail.com</a>, and feel free to address any questions and concerns as well.
</p>

<ul>
  <li>
    <a href="/files/2015_GLCACS_Annual_Conference_Announcement.pdf">
      <b>GLCACS_19th_Annual_Conference_Announcement</b> 
    </a>
  </li>

  <li>Student Presentation Registration Guide and 
  Application Form (<a href="/files/2015_GLCACS_Annual_Meeting_Student_Presentation_Registration_and_Guide.docx">
      docx</a>)
  </li>
</ul>
<br>
'''

conf_registration_form_html = '''
<h4>To check if you have registered, <a href="/conference_registration/check_registration">click here.</a></h4>   

<!--To show the registration form, remove the comment tag for the following form  -->
            
<br>
<h4>Step 1. Online Registration Form</h4> 

<form role="form" name="reg_conf_form" method="post" action="/conference_registration/add_record">

    <div class="form-group">
      <label>Name*</label>
      <input class="form-control" type="text" name="name" maxlength="50"  ng-model='name'  required>
    </div><!-- .form-group -->

    <div class="form-group">
      <label>Email*</label>
      <input class="form-control" type="email" name="email" maxlength="50" ng-model='email'  required>
    </div><!-- .form-group -->

    <div class="form-group">
      <label>Affiliation*</label>
      <input class="form-control" type="text" name="affiliation" maxlength="50"  ng-model='affiliation'  required>
    </div><!-- .form-group -->

    <div class="form-group">
      <label>Comments</label>

      <textarea class="form-control" name="comments" maxlength="1000"  rows="5" ng-model='comments'></textarea>
    </div><!-- .form-group -->
    <input type="submit" class="btn btn-default" name="submit" value="Submit" ng-disabled='reg_conf_form.$invalid'>
    <input type="reset" class="btn btn-default" value="Reset">
</form>
'''

submit_abs_link_html = '''
<h3><a href="/conference_registration/submit_form">
  Submit your abstract (file shoule less than 1M)
</a></h3>
'''