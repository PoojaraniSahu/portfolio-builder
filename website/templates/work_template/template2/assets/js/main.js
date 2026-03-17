/**
* Template Name: Laura
* Template URL: https://bootstrapmade.com/laura-free-creative-bootstrap-theme/
* Updated: Mar 17 2024 with Bootstrap v5.3.3
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/

(function() {
  "use strict";

  /**
   * Easy selector helper function
   */
  const select = (el, all = false) => {
    el = el.trim()
    if (all) {
      return [...document.querySelectorAll(el)]
    } else {
      return document.querySelector(el)
    }
  }

  /**
   * Easy event listener function
   */
  const on = (type, el, listener, all = false) => {
    let selectEl = select(el, all)
    if (selectEl) {
      if (all) {
        selectEl.forEach(e => e.addEventListener(type, listener))
      } else {
        selectEl.addEventListener(type, listener)
      }
    }
  }

  /**
   * Easy on scroll event listener 
   */
  const onscroll = (el, listener) => {
    el.addEventListener('scroll', listener)
  }

  /**
   * Navbar links active state on scroll
   */
  let navbarlinks = select('#navbar .scrollto', true)
  const navbarlinksActive = () => {
    let position = window.scrollY + 200
    navbarlinks.forEach(navbarlink => {
      if (!navbarlink.hash) return
      let section = select(navbarlink.hash)
      if (!section) return
      if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
        navbarlink.classList.add('active')
      } else {
        navbarlink.classList.remove('active')
      }
    })
  }
  window.addEventListener('load', navbarlinksActive)
  onscroll(document, navbarlinksActive)

  /**
   * Scrolls to an element with header offset
   */
  const scrollto = (el) => {
    let header = select('#header')
    let offset = header.offsetHeight

    if (!header.classList.contains('header-scrolled')) {
      offset -= 20
    }

    let elementPos = select(el).offsetTop
    window.scrollTo({
      top: elementPos - offset,
      behavior: 'smooth'
    })
  }

  /**
   * Toggle .header-scrolled class to #header when page is scrolled
   */
  let selectHeader = select('#header')
  if (selectHeader) {
    const headerScrolled = () => {
      if (window.scrollY > 100) {
        selectHeader.classList.add('header-scrolled')
      } else {
        selectHeader.classList.remove('header-scrolled')
      }
    }
    window.addEventListener('load', headerScrolled)
    onscroll(document, headerScrolled)
  }

  /**
   * Back to top button
   */
  let backtotop = select('.back-to-top')
  if (backtotop) {
    const toggleBacktotop = () => {
      if (window.scrollY > 100) {
        backtotop.classList.add('active')
      } else {
        backtotop.classList.remove('active')
      }
    }
    window.addEventListener('load', toggleBacktotop)
    onscroll(document, toggleBacktotop)
  }

  /**
   * Mobile nav toggle
   */
  on('click', '.mobile-nav-toggle', function(e) {
    select('#navbar').classList.toggle('navbar-mobile')
    this.classList.toggle('bi-list')
    this.classList.toggle('bi-x')
  })

  /**
   * Mobile nav dropdowns activate
   */
  on('click', '.navbar .dropdown > a', function(e) {
    if (select('#navbar').classList.contains('navbar-mobile')) {
      e.preventDefault()
      this.nextElementSibling.classList.toggle('dropdown-active')
    }
  }, true)

  /**
   * Scrool with ofset on links with a class name .scrollto
   */
  on('click', '.scrollto', function(e) {
    if (select(this.hash)) {
      e.preventDefault()

      let navbar = select('#navbar')
      if (navbar.classList.contains('navbar-mobile')) {
        navbar.classList.remove('navbar-mobile')
        let navbarToggle = select('.mobile-nav-toggle')
        navbarToggle.classList.toggle('bi-list')
        navbarToggle.classList.toggle('bi-x')
      }
      scrollto(this.hash)
    }
  }, true)

  /**
   * Scroll with ofset on page load with hash links in the url
   */
  window.addEventListener('load', () => {
    if (window.location.hash) {
      if (select(window.location.hash)) {
        scrollto(window.location.hash)
      }
    }
  });

  /**
   * Skills animation
   */
  let skilsContent = select('.skills-content');
  if (skilsContent) {
    new Waypoint({
      element: skilsContent,
      offset: '80%',
      handler: function(direction) {
        let progress = select('.progress .progress-bar', true);
        progress.forEach((el) => {
          el.style.width = el.getAttribute('aria-valuenow') + '%'
        });
      }
    })
  }

  /**
   * Testimonials slider
   */
  new Swiper('.testimonials-slider', {
    speed: 600,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    slidesPerView: 'auto',
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    }
  });

  /**
   * Porfolio isotope and filter
   */
  window.addEventListener('load', () => {
    let portfolioContainer = select('.portfolio-container');
    if (portfolioContainer) {
      let portfolioIsotope = new Isotope(portfolioContainer, {
        itemSelector: '.portfolio-item'
      });

      let portfolioFilters = select('#portfolio-flters li', true);

      on('click', '#portfolio-flters li', function(e) {
        e.preventDefault();
        portfolioFilters.forEach(function(el) {
          el.classList.remove('filter-active');
        });
        this.classList.add('filter-active');

        portfolioIsotope.arrange({
          filter: this.getAttribute('data-filter')
        });

      }, true);
    }

  });

  /**
   * Initiate portfolio lightbox 
   */
  const portfolioLightbox = GLightbox({
    selector: '.portfolio-lightbox'
  });

  /**
   * Portfolio details slider
   */
  new Swiper('.portfolio-details-slider', {
    speed: 400,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    }
  });

  /**
   * Initiate Pure Counter 
   */
  new PureCounter();

})()

let display=1;
function popup(){
    skillitem=document.getElementById("skd1");
    skillbtn=document.getElementById("skbtn");
    if(display==1){
        skillitem.classList.add("popup");
        display=0;
    }
    else{
        skillitem.classList.remove("popup");
        display=1;
    }

}
function addExperience() {
  var experienceInputs = document.getElementById("experienceInputs");
  var newExperience = document.createElement("div");
  newExperience.classList.add("experience");
  newExperience.innerHTML = `
  <input type="text" name="titles[]"  class="inp" placeholder="Title"><br>
  <input type="text" name="years[]" class="inp" placeholder="Year"><br>
  <input type="text" name="companies[]" class="inp" placeholder="Company"><br>
  <input type="text" name="descs[]" class="inp" placeholder="Description">
  <button type="button" class="bts rem" onclick="removeExperience(this)">Remove Experience</button>
  `;
  experienceInputs.appendChild(newExperience);
}
function removeExperience(button){
  var expdiv=button.parentNode;
  expdiv.parentNode.removeChild(expdiv);
}
function addSkill() {
  var sInputs = document.getElementById("skillInputs");
  var newS = document.createElement("div");
  newS.classList.add("skills");
  newS.innerHTML = `
  <input type="text" name="skill[]"  class="inp" placeholder="Skill"><br>
  <input type="text" name="perc[]" class="inp" placeholder="Percentage"><br>
  <button type="button" class="bts remS" onclick="removeSkill(this)">Remove Skill</button>
  `;
  sInputs.appendChild(newS);
}
function removeSkill(button){
  var sdiv=button.parentNode;
  sdiv.parentNode.removeChild(sdiv);
}
function addEdu() {
  var eduInputs = document.getElementById("eduInputs");
  var newEdu = document.createElement("div");
  newEdu.classList.add("education");
  newEdu.innerHTML = `
  <input type="text" name="couorse[]"  class="inp" placeholder="Course Name"><br>
  <input type="text" name="year[]" class="inp" placeholder="Year(from and to with - separator)"><br>
  <input type="text" name="institute[]" class="inp" placeholder="Institute"><br>
  <input type="text" name="desc[]" class="inp" placeholder="Description">
  <button type="button" class="bts rem" onclick="removeEdu(this)">Remove Education</button>
  `;
  eduInputs.appendChild(newEdu);
}
function removeEdu(button){
  var edudiv=button.parentNode;
  edudiv.parentNode.removeChild(edudiv);
}

var form1=document.getElementById("form1");
var form2=document.getElementById("form2");
var form3=document.getElementById("form3");
var form4=document.getElementById("form4");

var next1=document.getElementById("next1");
var next2=document.getElementById("next2");
var next3=document.getElementById("next3");
var back1=document.getElementById("back1");
var back2=document.getElementById("back2");
var back3=document.getElementById("back3");

var progressb=document.getElementById("prog");

next1.onclick=function(){
  form1.style.left="-1100px";
  form2.style.left="40px"
  progressb.style.width="37vw"
}
back1.onclick=function(){
  form1.style.left="40px";
  form2.style.left="1100px"
  progressb.style.width="18.5vw"
}

next2.onclick=function(){
  form2.style.left="-1100px";
  form3.style.left="40px"
  progressb.style.width="55.5vw"
}
back2.onclick=function(){
  form2.style.left="40px";
  form3.style.left="1100px"
  progressb.style.width="37vw"
}

next3.onclick=function(){
  form3.style.left="-1100px";
  form4.style.left="40px"
  progressb.style.width="74vw"
}
back3.onclick=function(){
  form3.style.left="40px";
  form4.style.left="1100px"
  progressb.style.width="55.5vw"
}