document.addEventListener('DOMContentLoaded', function() {

  const menuIcon = document.querySelector('.fa-bars');
  const nav = document.querySelector('nav');

  // Toggle the menu when clicking on the icon
  menuIcon.addEventListener('click', function() {
    this.classList.toggle('fa-times');
    nav.classList.toggle('nav-toggle');
  });

  // Remove classes when scrolling or loading the page
  window.addEventListener('scroll', function() {
    menuIcon.classList.remove('fa-times');
    nav.classList.remove('nav-toggle');
  });

  window.addEventListener('load', function() {
    menuIcon.classList.remove('fa-times');
    nav.classList.remove('nav-toggle');
  });

});
