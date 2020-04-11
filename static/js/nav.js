document.write(`
<div class="container-fluid nav-container hide-in-mobile">
		<div class="row">
			<div class=" col-md-1 dropdown">
				<a href="/index.html"><button class="dropbtn"> Home  </button></a>
			</div>
			<div class=" col-md-1 dropdown">
				<button class="dropbtn">Admission</button>
				<div class="dropdown-content">
					<a href="/admission/degree/degree.html">Engineering Degree</a>
					<a href="/admission/diploma/diploma.html">Engineering Diploma</a>
				</div>
			</div>
			<div class=" col-md-1 dropdown">
				<button class="dropbtn">Courses</button>
				<div class="dropdown-content">
					<a href="#" class="courses-heading">Engineering Degree</a>
					<a href="/pages/dept/degree/civil/civilHome.html">Civil</a>
					<a href="/pages/dept/degree/comps/compsHome.html">Computer</a>
					<a href="/pages/dept/degree/extc/extcHome.html">Electronics and Telecommunication</a>
					<a href="/pages/dept/degree/it/itHome.html">Information Technology</a>
					<a href="/pages/dept/degree/mech/mechHome.html">Mechanical</a>
					<a href="#" class="courses-heading">Engineering Diploma</a>
					<a href="#">Civil</a>
					<a href="#">Electronics and Telecommunication</a>
					<a href="#">Mechanical</a>
				</div>
			</div>
			<div class=" col-md-1 dropdown">
				<a href="/pages/committees.html"><button class="dropbtn">Committees</button></a>
			</div>
			<div class=" col-md-1 dropdown">
				<a href="/pages/gallery.html"> <button class="dropbtn">Gallery</button> </a>
			</div>
			<div class=" col-md-1 dropdown">
				<a href="/pages/aboutus.html"> <button class="dropbtn">AboutUs</button> </a>
			</div>
		</div>
	</div>




	<div class="container-fluid responsive-nav">
		<div class="row nav-resp-title-btn-row">
			<div class="col-sm-3 element-center resp-nav-title">SJCEM</div>
			<div class="col-sm-9 nav-resp-btn-container">
					<i class="fa fa-bars resp-btn"></i>
			</div>
			<div class="col-sm-12 nav-resp-menus-cont">
				<ul class="main-menu-ul">
					<li><a href="/index.html">Home</a></li>
					<li id="admission-menu">Admission
						<ul class="responsive-submenu" id="admission-menus">
							<li><a href="/admission/degree/degree.html">Engineering Degree</a></li>
							<li>Engineering Diploma</li>
						</ul>
						
					</li>
					<li id="courses-menu">Courses
						<ul class="responsive-submenu" id="courses-menus">
							<li href="#" class="courses-heading">Engineering Degree</li>
							<li> <a href="/pages/dept/degree/civil/civilHome.html"> Civil </a> </li>
							<li> <a href="/pages/dept/degree/comps/compsHome.html"> Computer </a> </li>
							<li> <a href="/pages/dept/degree/extc/extcHome.html"> Electronics and Telecommunication </a> </li>
							<li> <a  href="/pages/dept/degree/it/itHome.html"> Information Technology </a></li>
							<li> <a href="/pages/dept/degree/mech/mechHome.html"> Mechanical </a> </li>
							<li href="#" class="courses-heading">Engineering Diploma</li>
							<li><a href="">Civil</a></li>
							<li><a href="">Electronics and Telecommunication</a></li>
							<li><a href="">Mechanical</a></li>
						</ul>
					</li>
					<li><a href="/pages/committees.html"></a>Committes</li>
					<li><a href="/pages/gallery.html"></a>Gallery</li>
					<li><a href="/pages/aboutus.html">AboutUs</a></li>
				</ul>
			</div>
		</div>
	</div>




	<div class="container-fluid name-logo-container">
		<div class="row logo-bar-container">
			<div class="col-md-2 col-sm-12 logo-img-container"> <img src="/img/logo.gif" class="logo-img"></div>
			<div class="col-md-10 col-sm-12 college-name">
				<h4> Aldel Education Trust's </h4>
				<h3>St. John College Of Engineering And Management</h3>
				<h5>Palghar (East)   Dist. Palghar</h5>
				<h5>Approved by AICTE, DTE and affiliated to the University of Mumbai, MSBTE</h5>
			</div>
		</div>
	</div>
	`);