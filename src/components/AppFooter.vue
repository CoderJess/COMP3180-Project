<template>
    <footer class="site-footer">
      <div class="container-fluid footer-container">
        <div class="row footer-content">
          <div class="col-md-4 footer-brand">
            <h3>Jam + Date</h3>
            <p class="tagline">Find your perfect flavor match</p>
          </div>
          <div class="col-md-4 footer-links">
            <h4>Quick Links</h4>
            <ul>
              <li><RouterLink to="/about">About Us</RouterLink></li>
              <li><RouterLink to="/profiles/new">Create Profile</RouterLink></li>
            </ul>
          </div>
          <div class="col-md-4 footer-social">
            <h4>Connect With Us</h4>
            <div class="social-icons">
              <a href="#" aria-label="Facebook"><i class="bi bi-facebook"></i></a>
              <a href="#" aria-label="Instagram"><i class="bi bi-instagram"></i></a>
              <a href="#" aria-label="Twitter"><i class="bi bi-twitter"></i></a>
            </div>
          </div>
        </div>
        <div class="footer-bottom">
          <p>Copyright &copy; {{ year }} Jam + Date. All rights reserved.</p>
        </div>
      </div>
    </footer>
  </template>
  
  <script setup>
  import { ref } from "vue";
  
  const year = new Date().getFullYear();
  </script>
  
  <style>
  /* Footer Styling */
  .site-footer {
    background: linear-gradient(135deg, #331f12 0%, #5a3d28 100%);
    padding: 3rem 0 1rem;
    color: #f0f0f0;
    box-shadow: 0 -2px 15px rgba(0, 0, 0, 0.2);
    margin-top: 4rem;
    position: relative;
  }
  
  .site-footer::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: linear-gradient(90deg, transparent, #ffd700 30%, #ffd700 70%, transparent);
  }
  
  .footer-container {
    width: 90%;
    margin: 0 auto;
  }
  
  .footer-content {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    margin-bottom: 2rem;
  }
  
  /* Footer Brand Section */
  .footer-brand h3 {
    color: #ffd700;
    font-weight: 800;
    font-size: 1.7rem;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
  }
  
  .footer-brand .tagline {
    font-style: italic;
    color: #d4c5b3;
  }
  
  /* Footer Links Section */
  .footer-links h4, .footer-social h4 {
    color: #ffd700;
    font-size: 1.2rem;
    margin-bottom: 1rem;
    position: relative;
    display: inline-block;
  }
  
  .footer-links h4::after, .footer-social h4::after {
    content: "";
    position: absolute;
    bottom: -5px;
    left: 0;
    width: 50%;
    height: 2px;
    background: linear-gradient(90deg, #ffd700, transparent);
  }
  
  .footer-links ul {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  
  .footer-links ul li {
    margin-bottom: 0.8rem;
  }
  
  .footer-links ul li a {
    color: #f0f0f0;
    text-decoration: none;
    transition: all 0.3s ease;
    position: relative;
    padding-left: 15px;
  }
  
  .footer-links ul li a::before {
    content: "•";
    color: #ffd700;
    position: absolute;
    left: 0;
    top: 0;
  }
  
  .footer-links ul li a:hover {
    color: #ffd700;
    transform: translateX(5px);
  }
  
  /* Footer Social Section */
  .social-icons {
    display: flex;
    gap: 1rem;
  }
  
  .social-icons a {
    color: #f0f0f0;
    font-size: 1.5rem;
    transition: all 0.3s ease;
    display: inline-block;
  }
  
  .social-icons a:hover {
    color: #ffd700;
    transform: translateY(-3px);
  }
  
  /* Footer Bottom */
  .footer-bottom {
    border-top: 1px solid rgba(255, 215, 0, 0.2);
    padding-top: 1.5rem;
    text-align: center;
    color: #d4c5b3;
    font-size: 0.9rem;
  }
  
  /* Responsive Adjustments */
  @media (max-width: 991.98px) {
    .footer-content {
      flex-direction: column;
      text-align: center;
    }
  
    .footer-brand, .footer-links, .footer-social {
      margin-bottom: 2rem;
      width: 100%;
    }
  
    .footer-links h4::after, .footer-social h4::after {
      left: 50%;
      transform: translateX(-50%);
      width: 80px;
    }
  
    .footer-links ul li a {
      padding-left: 0;
    }
  
    .footer-links ul li a::before {
      display: none;
    }
  
    .social-icons {
      justify-content: center;
    }
  }
  
  /* For extra small devices */
  @media (max-width: 575.98px) {
    .site-footer {
      padding: 2rem 0 1rem;
    }
  }
  </style>