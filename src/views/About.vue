<template>
    <div class="about-page">
      <div class="container">
        <h1>About <span class="highlight">Jam-Date</span></h1>
        <div class="tagline">Connecting Jamaican hearts worldwide</div>
        
        <div class="mission-section">
          <h2>Our Mission</h2>
          <p>
            At Jam-Date, we're dedicated to connecting Jamaicans around the world through meaningful relationships. 
            Our platform celebrates Jamaican culture and values while providing a safe, authentic space for singles 
            to meet, connect, and build relationships rooted in shared heritage and experiences.
          </p>
        </div>
        
        <div class="story-section">
          <h2>Our Story</h2>
          <p>
            Jam-Date was born in 2025 when four college friends—Shaquille, Kelly, Samantha, and Ryon—noticed 
            the lack of dating platforms that truly understood Jamaican culture and dating preferences. As Jamaican 
            students studying abroad, they experienced firsthand the challenges of finding partners who appreciated 
            their cultural background. What began as a final-year project quickly evolved into a passion-driven 
            platform connecting Jamaicans across the globe.
          </p>
        </div>
        
        <div class="features-grid">
          <div class="feature-card">
            <div class="icon">🌴</div>
            <h3>Cultural Connection</h3>
            <p>Find matches who understand and appreciate Jamaican heritage, values, and traditions.</p>
          </div>
          
          <div class="feature-card">
            <div class="icon">🎉</div>
            <h3>Event Discovery</h3>
            <p>Connect at Jamaican cultural events, festivals, and gatherings near you.</p>
          </div>
          
          <div class="feature-card">
            <div class="icon">💬</div>
            <h3>Authentic Communication</h3>
            <p>Express yourself freely with patois-friendly chat features and cultural references.</p>
          </div>
          
          <div class="feature-card">
            <div class="icon">🔒</div>
            <h3>Safe Community</h3>
            <p>Verified profiles and strict moderation to protect our community members.</p>
          </div>
        </div>
        
        <div class="team-section">
          <h2>Meet Our Founders</h2>
          <div class="team-grid">
            <div class="team-member">
              <div class="member-avatar"></div>
              <h3>Shaquille</h3>
              <p>Co-Founder</p>
            </div>
            
            <div class="team-member">
              <div class="member-avatar"></div>
              <h3>Kelly</h3>
              <p>Co-Founder</p>
            </div>
            
            <div class="team-member">
              <div class="member-avatar"></div>
              <h3>Samantha</h3>
              <p>Co-Founder</p>
            </div>
            
            <div class="team-member">
              <div class="member-avatar"></div>
              <h3>Ryon</h3>
              <p>Co-Founder</p>
            </div>
          </div>
        </div>
        
        <div class="testimonial-section">
          <h2>The link is below</h2>
          <div class="testimonial">
            <p>"Let's make this more than just a click."</p>
            <div class="testimonial-author">— Someone in 2025😊</div>
          </div>
        </div>
        
        <div class="cta-section">
          <h2>Ready to find your perfect match?</h2>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "AboutPage"
  }
  </script>
  
  <style>
  :root {
    --black: #121212;
    --green: #1e8f4e;
    --gold: #d4af37;
    --light-gold: #f5e7b8;
    --dark-green: #146b3a;
  }
  
  .about-page {
    background-color: var(--black);
    color: white;
    font-family: "Segoe UI", Tahoma, sans-serif;
    padding: 40px 0 80px;
    min-height: 100vh;
  }
  
  .container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
  }
  
  h1 {
    font-size: 3rem;
    text-align: center;
    margin-bottom: 40px;
    color: white;
  }
  
  h2 {
    font-size: 2rem;
    color: var(--light-gold);
    margin-bottom: 20px;
    position: relative;
    padding-bottom: 10px;
  }
  
  h2::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 60px;
    height: 3px;
    background-color: var(--green);
  }
  
  .highlight {
    color: var(--gold);
    font-weight: bold;
  }
  
  .mission-section, .story-section, .team-section, .testimonial-section, .cta-section {
    margin-bottom: 60px;
  }
  
  .mission-section p, .story-section p {
    font-size: 1.2rem;
    line-height: 1.6;
    max-width: 800px;
  }
  
  .features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 30px;
    margin: 50px 0;
  }
  
  .feature-card {
    background-color: rgba(30, 30, 30, 0.6);
    border-radius: 10px;
    padding: 30px;
    text-align: center;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    border: 1px solid rgba(212, 175, 55, 0.2);
  }
  
  .feature-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
    border-color: var(--gold);
  }
  
  .icon {
    font-size: 2.5rem;
    margin-bottom: 15px;
  }
  
  .feature-card h3 {
    color: var(--green);
    margin-bottom: 15px;
    font-size: 1.3rem;
  }
  
  .team-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 40px;
    margin-top: 30px;
  }
  
  .team-member {
    text-align: center;
  }
  
  .member-avatar {
    width: 150px;
    height: 150px;
    border-radius: 50%;
    background-color: #333;
    margin: 0 auto 15px;
    border: 3px solid var(--gold);
    background-image: linear-gradient(45deg, #333, #222);
  }
  
  .team-member h3 {
    color: var(--light-gold);
    margin-bottom: 5px;
    font-size: 1.2rem;
  }
  
  .team-member p {
    color: var(--green);
    font-size: 1rem;
  }
  
  .testimonial {
    background-color: rgba(30, 30, 30, 0.6);
    border-radius: 10px;
    padding: 30px;
    position: relative;
    border-left: 4px solid var(--green);
    margin-top: 30px;
  }
  
  .testimonial p {
    font-size: 1.2rem;
    font-style: italic;
    line-height: 1.6;
  }
  
  .testimonial-author {
    color: var(--gold);
    text-align: right;
    margin-top: 20px;
    font-weight: bold;
  }
  
  .cta-section {
    text-align: center;
    background-color: rgba(30, 143, 78, 0.1);
    padding: 50px 20px;
    border-radius: 10px;
    margin-top: 60px;
  }
  
  .tagline {
    text-align: center;
    font-size: 1.4rem;
    color: var(--green);
    margin-top: -20px;
    margin-bottom: 40px;
    font-style: italic;
  }
  
  .cta-section h2 {
    text-align: center;
    margin-bottom: 30px;
  }
  
  .cta-section h2::after {
    left: 50%;
    transform: translateX(-50%);
    width: 100px;
  }
  
  .cta-button {
    display: inline-block;
    background-color: var(--green);
    color: white;
    padding: 15px 40px;
    border-radius: 8px;
    text-decoration: none;
    font-weight: bold;
    font-size: 1.2rem;
    transition: all 0.3s ease;
    border: 2px solid transparent;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
  
  .cta-button:hover {
    background-color: var(--dark-green);
    transform: translateY(-2px);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    border: 2px solid var(--gold);
  }
  
  @media (max-width: 768px) {
    .features-grid, .team-grid {
      grid-template-columns: 1fr;
    }
    
    h1 {
      font-size: 2.5rem;
    }
    
    h2 {
      font-size: 1.8rem;
    }
    
    .mission-section p, .story-section p, .testimonial p {
      font-size: 1.1rem;
    }
  }
  </style>