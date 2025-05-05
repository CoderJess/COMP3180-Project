<template>
    <footer class="footer">
      <div class="container">
        <div class="footer-content">
          <div class="footer-brand">
            <h3>Jamaica's #1 Dating site.</h3>
            <p class="tagline">Best place to find your perfect match.</p>
          </div>
          
          <div class="footer-links">
            <div class="link-group">
              <h4>Navigation</h4>
              <ul>
                <li><RouterLink to="/">Home</RouterLink></li>
                <li><RouterLink to="/about">About</RouterLink></li>
              </ul>
            </div>
            
            <div class="link-group">
              <h4>Resources</h4>
              <ul>
                <li><a href="https://vuejs.org/" target="_blank">Vue.js</a></li>
                <li><a href="https://flask.palletsprojects.com/" target="_blank">Flask</a></li>
              </ul>
            </div>
          </div>
        </div>
        
        <div class="footer-bottom">
          <p class="copyright">Copyright &copy; {{ year }} Flask Inc. All rights reserved.</p>
          <div class="social-icons">
            <a href="#" class="social-icon" aria-label="GitHub">
              <i class="fab fa-github"></i>
            </a>
            <a href="#" class="social-icon" aria-label="Twitter">
              <i class="fab fa-twitter"></i>
            </a>
            <a href="#" class="social-icon" aria-label="LinkedIn">
              <i class="fab fa-linkedin"></i>
            </a>
          </div>
        </div>
      </div>
    </footer>
  </template>
  
  <script setup>
  import { ref } from "vue";
  import { RouterLink } from "vue-router";
  
  const year = (new Date()).getFullYear();
  </script>
  
  <style>
  .footer {
    background-color: #343a40;
    color: #ffffff;
    padding: 3rem 0 1.5rem;
    margin-top: 5rem;
  }
  
  .footer-content {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    margin-bottom: 2rem;
  }
  
  .footer-brand {
    flex: 1;
    min-width: 250px;
    margin-bottom: 1.5rem;
  }
  
  .footer-brand h3 {
    font-size: 1.5rem;
    margin-bottom: 0.5rem;
    font-weight: 700;
  }
  
  .tagline {
    font-size: 0.9rem;
    color: rgba(255, 255, 255, 0.8);
  }
  
  .footer-links {
    display: flex;
    flex-wrap: wrap;
    gap: 2rem;
  }
  
  .link-group {
    min-width: 120px;
    margin-bottom: 1.5rem;
  }
  
  .link-group h4 {
    font-size: 1rem;
    margin-bottom: 1rem;
    font-weight: 600;
    color: #ffffff;
  }
  
  .link-group ul {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  
  .link-group li {
    margin-bottom: 0.5rem;
  }
  
  .link-group a {
    color: rgba(255, 255, 255, 0.8);
    text-decoration: none;
    font-size: 0.9rem;
    transition: color 0.2s ease;
  }
  
  .link-group a:hover {
    color: #ffffff;
    text-decoration: underline;
  }
  
  .footer-bottom {
    padding-top: 1.5rem;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
  }
  
  .copyright {
    font-size: 0.85rem;
    color: rgba(255, 255, 255, 0.7);
    margin: 0;
  }
  
  .social-icons {
    display: flex;
    gap: 1rem;
  }
  
  .social-icon {
    color: rgba(255, 255, 255, 0.8);
    font-size: 1.2rem;
    transition: all 0.2s ease;
  }
  
  .social-icon:hover {
    color: #ffffff;
    transform: translateY(-3px);
  }
  
  /* Responsive adjustments */
  @media (max-width: 768px) {
    .footer-content {
      flex-direction: column;
    }
    
    .footer-bottom {
      flex-direction: column;
      text-align: center;
      gap: 1rem;
    }
  }
  </style>