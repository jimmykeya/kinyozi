import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import time

# Configure the page
st.set_page_config(
    page_title="Classic Executive Barber Shop",
    page_icon="✂️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for beautiful blue-themed styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Roboto:wght@300;400;500&display=swap');
    
    .main {
        padding-top: 2rem;
    }
    
    .stSelectbox {
        display: none;
    }
    
    .navigation-header {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 50%, #4a90e2 100%);
        padding: 1rem 0;
        margin: -1rem -1rem 2rem -1rem;
        border-radius: 0 0 20px 20px;
        box-shadow: 0 4px 20px rgba(30, 60, 114, 0.3);
    }
    
    .nav-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 2rem;
    }
    
    .brand-section {
        text-align: center;
        color: white;
        margin-bottom: 1.5rem;
    }
    
    .brand-title {
        font-family: 'Playfair Display', serif;
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .brand-subtitle {
        font-family: 'Roboto', sans-serif;
        font-size: 1rem;
        opacity: 0.9;
        font-style: italic;
        margin: 0;
    }
    
    .nav-menu {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 0.5rem;
        margin-top: 1rem;
    }
    
    .nav-item {
        background: rgba(255, 255, 255, 0.1);
        border: 2px solid rgba(255, 255, 255, 0.2);
        color: white;
        padding: 0.8rem 1.5rem;
        border-radius: 25px;
        text-decoration: none;
        font-family: 'Roboto', sans-serif;
        font-weight: 500;
        transition: all 0.3s ease;
        cursor: pointer;
        backdrop-filter: blur(10px);
        font-size: 0.9rem;
    }
    
    .nav-item:hover {
        background: rgba(255, 255, 255, 0.2);
        border-color: rgba(255, 255, 255, 0.4);
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    .nav-item.active {
        background: linear-gradient(135deg, #ffffff 0%, #f0f8ff 100%);
        color: #1e3c72;
        border-color: white;
        font-weight: 600;
    }
    
    .main-header {
        font-family: 'Playfair Display', serif;
        font-size: 3rem;
        color: #1e3c72;
        text-align: center;
        margin: 2rem 0;
        text-shadow: 2px 2px 4px rgba(30, 60, 114, 0.1);
    }
    
    .sub-header {
        font-family: 'Playfair Display', serif;
        font-size: 2rem;
        color: #2a5298;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .service-card {
        background: linear-gradient(135deg, #f8fbff 0%, #e6f3ff 100%);
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 5px solid #4a90e2;
        margin: 1rem 0;
        box-shadow: 0 8px 25px rgba(74, 144, 226, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        font-family: 'Roboto', sans-serif;
    }
    
    .service-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 35px rgba(74, 144, 226, 0.2);
    }
    
    .price-tag {
        font-size: 1.5rem;
        font-weight: bold;
        color: #1e3c72;
        float: right;
        background: linear-gradient(135deg, #e6f3ff 0%, #cce7ff 100%);
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        border: 2px solid #4a90e2;
    }
    
    .hero-section {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 50%, #4a90e2 100%);
        color: white;
        padding: 4rem 2rem;
        border-radius: 20px;
        text-align: center;
        margin: 2rem 0;
        box-shadow: 0 15px 35px rgba(30, 60, 114, 0.3);
        font-family: 'Roboto', sans-serif;
    }
    
    .hero-title {
        font-family: 'Playfair Display', serif;
        font-size: 3.5rem;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .hero-subtitle {
        font-size: 1.5rem;
        margin-bottom: 2rem;
        opacity: 0.9;
        font-weight: 300;
    }
    
    .testimonial {
        background: linear-gradient(135deg, #f0f8ff 0%, #e0f0ff 100%);
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 4px solid #4a90e2;
        margin: 1rem 0;
        font-style: italic;
        font-family: 'Roboto', sans-serif;
        box-shadow: 0 5px 15px rgba(74, 144, 226, 0.1);
    }
    
    .contact-info {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        font-family: 'Roboto', sans-serif;
        box-shadow: 0 10px 25px rgba(30, 60, 114, 0.3);
    }
    
    .booking-form {
        background: linear-gradient(135deg, #f8fbff 0%, #e6f3ff 100%);
        padding: 2rem;
        border-radius: 15px;
        border: 2px solid #4a90e2;
        font-family: 'Roboto', sans-serif;
        box-shadow: 0 10px 25px rgba(74, 144, 226, 0.1);
    }
    
    .metric-card {
        background: linear-gradient(135deg, #ffffff 0%, #f0f8ff 100%);
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        border: 2px solid #e6f3ff;
        box-shadow: 0 5px 15px rgba(74, 144, 226, 0.1);
    }
    
    .feature-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8fbff 100%);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        border: 2px solid #e6f3ff;
        height: 100%;
        transition: transform 0.3s ease;
        font-family: 'Roboto', sans-serif;
        box-shadow: 0 8px 25px rgba(74, 144, 226, 0.1);
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
    }
    
    .special-package {
        background: linear-gradient(135deg, #4a90e2 0%, #2a5298 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 10px 25px rgba(74, 144, 226, 0.3);
    }
    
    .gold-package {
        background: linear-gradient(135deg, #ffd700 0%, #ffed4e 100%);
        color: #1e3c72;
    }
    
    .footer {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        color: white;
        padding: 3rem 2rem;
        border-radius: 20px 20px 0 0;
        text-align: center;
        margin-top: 3rem;
        font-family: 'Roboto', sans-serif;
    }
</style>
""", unsafe_allow_html=True)

# Navigation function
def create_navigation():
    st.markdown("""
    <div class="navigation-header">
        <div class="nav-container">
            <div class="brand-section">
                <h1 class="brand-title">✂️ CLASSIC EXECUTIVE BARBER SHOP</h1>
                <p class="brand-subtitle">"Where Style Meets Tradition"</p>
            </div>
            <div class="nav-menu">
                <div class="nav-item" onclick="changePage('🏠 Home')">🏠 Home</div>
                <div class="nav-item" onclick="changePage('✂️ Services')">✂️ Services & Pricing</div>
                <div class="nav-item" onclick="changePage('📅 Booking')">📅 Book Appointment</div>
                <div class="nav-item" onclick="changePage('👨‍💼 About')">👨‍💼 About Us</div>
                <div class="nav-item" onclick="changePage('📸 Gallery')">📸 Gallery</div>
                <div class="nav-item" onclick="changePage('📞 Contact')">📞 Contact</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Initialize session state for navigation
if 'current_page' not in st.session_state:
    st.session_state.current_page = '🏠 Home'

# Create navigation
create_navigation()

# Page selection buttons (hidden but functional)
col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    if st.button("🏠", help="Home", key="home_btn"):
        st.session_state.current_page = '🏠 Home'
with col2:
    if st.button("✂️", help="Services", key="services_btn"):
        st.session_state.current_page = '✂️ Services'
with col3:
    if st.button("📅", help="Booking", key="booking_btn"):
        st.session_state.current_page = '📅 Booking'
with col4:
    if st.button("👨‍💼", help="About", key="about_btn"):
        st.session_state.current_page = '👨‍💼 About'
with col5:
    if st.button("📸", help="Gallery", key="gallery_btn"):
        st.session_state.current_page = '📸 Gallery'
with col6:
    if st.button("📞", help="Contact", key="contact_btn"):
        st.session_state.current_page = '📞 Contact'

# Get current page
page = st.session_state.current_page

# Home Page
if page == '🏠 Home':
    # Hero Section
    st.markdown("""
    <div class="hero-section">
        <h1 class="hero-title">Welcome to Excellence</h1>
        <h2 class="hero-subtitle">Premium Grooming for the Modern Gentleman</h2>
        <p style="font-size: 1.2rem; line-height: 1.6; max-width: 800px; margin: 0 auto;">
            Experience the finest in traditional barbering with a contemporary twist. 
            Our master barbers combine time-honored techniques with modern style to deliver 
            the perfect cut, shave, and grooming experience that exceeds expectations.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Key Features
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3 style="color: #1e3c72; font-size: 1.5rem; margin-bottom: 1rem;">🏆 Master Craftsmen</h3>
            <p style="color: #555; line-height: 1.6;">Certified professionals with over 10 years of experience in precision cutting and traditional barbering techniques.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3 style="color: #1e3c72; font-size: 1.5rem; margin-bottom: 1rem;">💎 Premium Experience</h3>
            <p style="color: #555; line-height: 1.6;">Luxury grooming products, state-of-the-art equipment, and an atmosphere of refined elegance.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h3 style="color: #1e3c72; font-size: 1.5rem; margin-bottom: 1rem;">⏰ Flexible Service</h3>
            <p style="color: #555; line-height: 1.6;">Open 7 days a week with extended hours to accommodate your busy executive schedule.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Statistics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #1e3c72; font-size: 2rem; margin: 0;">2,500+</h3>
            <p style="color: #666; margin: 0;">Happy Clients</p>
            <p style="color: #4a90e2; font-size: 0.9rem; margin: 0;">Growing Daily</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #1e3c72; font-size: 2rem; margin: 0;">15</h3>
            <p style="color: #666; margin: 0;">Years Excellence</p>
            <p style="color: #4a90e2; font-size: 0.9rem; margin: 0;">And Counting</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #1e3c72; font-size: 2rem; margin: 0;">5</h3>
            <p style="color: #666; margin: 0;">Master Barbers</p>
            <p style="color: #4a90e2; font-size: 0.9rem; margin: 0;">Expert Team</p>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #1e3c72; font-size: 2rem; margin: 0;">4.9★</h3>
            <p style="color: #666; margin: 0;">Customer Rating</p>
            <p style="color: #4a90e2; font-size: 0.9rem; margin: 0;">Excellent Service</p>
        </div>
        """, unsafe_allow_html=True)

elif page == '✂️ Services':
    st.markdown('<h1 class="main-header">Our Premium Services</h1>', unsafe_allow_html=True)
    
    # Services with pricing
    services = [
        {
            "name": "✂️ Executive Haircut",
            "description": "Precision cut tailored to your style and face shape. Includes consultation, wash, cut, and professional styling.",
            "duration": "45 min",
            "price": "KSh 1,500"
        },
        {
            "name": "🪒 Traditional Wet Shave",
            "description": "Classic hot towel shave with premium razors, rich lathers, and soothing aftercare treatment.",
            "duration": "30 min",
            "price": "KSh 1,200"
        },
        {
            "name": "👨‍💼 The Executive Package",
            "description": "Complete grooming experience: haircut, beard trim, eyebrow grooming, and relaxing hot towel treatment.",
            "duration": "90 min",
            "price": "KSh 2,800"
        },
        {
            "name": "🧔 Beard Trim & Styling",
            "description": "Professional beard shaping and styling with premium oils, balms, and precision trimming techniques.",
            "duration": "25 min",
            "price": "KSh 800"
        },
        {
            "name": "👦 Kids Haircut",
            "description": "Gentle, patient service for children under 12. Fun, stress-free experience with special attention to comfort.",
            "duration": "30 min",
            "price": "KSh 900"
        },
        {
            "name": "💆‍♂️ Scalp Treatment",
            "description": "Relaxing scalp massage with therapeutic oils and revitalizing treatments for healthy hair growth.",
            "duration": "20 min",
            "price": "KSh 600"
        }
    ]
    
    for service in services:
        st.markdown(f"""
        <div class="service-card">
            <h3 style="color: #1e3c72; margin-bottom: 0.5rem;">{service['name']} <span class="price-tag">{service['price']}</span></h3>
            <p style="color: #4a90e2; font-weight: 500; margin: 0.5rem 0;"><strong>Duration:</strong> {service['duration']}</p>
            <p style="color: #555; line-height: 1.6; margin: 0;">{service['description']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Special Packages
    st.markdown('<h2 class="sub-header">🎁 Exclusive Packages</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="special-package gold-package">
            <h3 style="margin-top: 0;">🌟 VIP Membership</h3>
            <h2 style="font-size: 2rem; margin: 1rem 0;">KSh 8,000/month</h2>
            <ul style="text-align: left; line-height: 1.8;">
                <li>Unlimited executive haircuts</li>
                <li>2 traditional wet shaves</li>
                <li>Priority booking privileges</li>
                <li>Complimentary scalp treatments</li>
                <li>10% discount on additional services</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="special-package">
            <h3 style="margin-top: 0;">💼 Corporate Package</h3>
            <h2 style="font-size: 1.5rem; margin: 1rem 0;">Group Discounts Available</h2>
            <ul style="text-align: left; line-height: 1.8;">
                <li>Team grooming sessions</li>
                <li>On-site corporate services</li>
                <li>Flexible group scheduling</li>
                <li>Volume pricing discounts</li>
                <li>Executive event grooming</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

elif page == '📅 Booking':
    st.markdown('<h1 class="main-header">Book Your Appointment</h1>', unsafe_allow_html=True)
    
    st.markdown('<div class="booking-form">', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📋 Personal Information")
        
        name = st.text_input("👤 Full Name*", placeholder="Enter your full name")
        phone = st.text_input("📱 Phone Number*", placeholder="+254 7XX XXX XXX")
        email = st.text_input("📧 Email Address", placeholder="your.email@example.com")
        
        st.markdown("### ✂️ Service Selection")
        service_options = [
            "Executive Haircut - KSh 1,500",
            "Traditional Wet Shave - KSh 1,200", 
            "The Executive Package - KSh 2,800",
            "Beard Trim & Styling - KSh 800",
            "Kids Haircut - KSh 900",
            "Scalp Treatment - KSh 600"
        ]
        
        selected_service = st.selectbox("Choose Your Service*", service_options)
        
        barber_options = ["No Preference", "Master James", "Master Peter", "Master David", "Master Samuel", "Master Michael"]
        preferred_barber = st.selectbox("👨‍💼 Preferred Barber", barber_options)
    
    with col2:
        st.markdown("### 📅 Schedule Details")
        
        min_date = datetime.now().date()
        max_date = min_date + timedelta(days=30)
        selected_date = st.date_input("📅 Preferred Date*", min_value=min_date, max_value=max_date)
        
        time_slots = [
            "9:00 AM", "9:30 AM", "10:00 AM", "10:30 AM", "11:00 AM", "11:30 AM",
            "12:00 PM", "12:30 PM", "1:00 PM", "1:30 PM", "2:00 PM", "2:30 PM",
            "3:00 PM", "3:30 PM", "4:00 PM", "4:30 PM", "5:00 PM", "5:30 PM",
            "6:00 PM", "6:30 PM", "7:00 PM"
        ]
        
        selected_time = st.selectbox("🕐 Preferred Time*", time_slots)
        
        st.markdown("### 💬 Additional Information")
        special_requests = st.text_area("Special Requests or Preferences", 
                                      placeholder="Any specific requirements, hair concerns, or styling preferences...",
                                      height=100)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Booking button
    if st.button("📅 CONFIRM BOOKING", type="primary", use_container_width=True):
        if name and phone and selected_service:
            with st.spinner("Processing your appointment..."):
                time.sleep(2)
            
            st.success(f"""
            ✅ **Appointment Successfully Booked!**
            
            **Customer:** {name}
            **Service:** {selected_service}
            **Date:** {selected_date.strftime('%A, %B %d, %Y')}
            **Time:** {selected_time}
            **Barber:** {preferred_barber}
            
            📱 Confirmation SMS sent to {phone}
            📧 Email confirmation sent to {email if email else 'Not provided'}
            
            **Please arrive 10 minutes early for your appointment.**
            """)
            
            st.info("""
            📞 **Need Changes?** Call us at +254 712 345 678
            ⏰ **Cancellation Policy:** 24-hour notice required
            🚗 **Parking:** Complimentary parking available
            """)
        else:
            st.error("⚠️ Please fill in all required fields marked with *")

elif page == '👨‍💼 About':
    st.markdown('<h1 class="main-header">About Classic Executive Barber Shop</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="service-card">
        <h3 style="color: #1e3c72;">🏛️ Our Heritage</h3>
        <p style="line-height: 1.8; color: #555;">
        Founded in 2008, Classic Executive Barber Shop has established itself as Nairobi's premier 
        destination for discerning gentlemen who value excellence in grooming. We blend traditional 
        barbering artistry with contemporary techniques to create an unparalleled experience.
        </p>
        </div>
        
        <div class="service-card">
        <h3 style="color: #1e3c72;">🎯 Our Mission</h3>
        <p style="line-height: 1.8; color: #555;">
        To provide every client with exceptional grooming services in a sophisticated, welcoming 
        environment where traditional craftsmanship meets modern innovation. We believe that great 
        grooming is an investment in confidence and success.
        </p>
        </div>
        
        <div class="service-card">
        <h3 style="color: #1e3c72;">💎 Excellence Standards</h3>
        <ul style="line-height: 1.8; color: #555;">
            <li><strong>Master Artisans:</strong> Skilled craftsmen dedicated to their art</li>
            <li><strong>Premium Quality:</strong> Only the finest tools and products</li>
            <li><strong>Personal Touch:</strong> Customized service for every client</li>
            <li><strong>Luxury Environment:</strong> Refined atmosphere for relaxation</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="contact-info">
            <h3>📊 Our Achievements</h3>
            <div style="margin: 1rem 0;">
                <h2 style="margin: 0.5rem 0; font-size: 2.5rem;">15+</h2>
                <p style="margin: 0;">Years of Excellence</p>
            </div>
            <div style="margin: 1rem 0;">
                <h2 style="margin: 0.5rem 0; font-size: 2.5rem;">2,500+</h2>
                <p style="margin: 0;">Satisfied Customers</p>
            </div>
            <div style="margin: 1rem 0;">
                <h2 style="margin: 0.5rem 0; font-size: 2.5rem;">8</h2>
                <p style="margin: 0;">Industry Awards</p>
            </div>
            <div style="margin: 1rem 0;">
                <h2 style="margin: 0.5rem 0; font-size: 2.5rem;">5</h2>
                <p style="margin: 0;">Master Barbers</p>
            </div>
        </div>
        
        <div style="margin-top: 2rem;">
        <div class="service-card">
            <h4 style="color: #1e3c72;">🏆 Recognition</h4>
            <ul style="color: #555; line-height: 1.6;">
                <li>Best Barber Shop Nairobi 2023</li>
                <li>Customer Service Excellence 2022</li>
                <li>Traditional Craftsmanship Award 2021</li>
                <li>Community Choice Award 2020</li>
            </ul>
        </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Team Section
    st.markdown('<h2 class="sub-header">👥 Meet Our Master Team</h2>', unsafe_allow_html=True)
    
    team_members = [
        {"name": "James Mwangi", "title": "Master Barber & Owner", "experience": "20 years", "specialty": "Classic cuts & traditional shaves"},
        {"name": "Peter Kiprotich", "title": "Senior Master Barber", "experience": "15 years", "specialty": "Modern styling & beard artistry"},
        {"name": "David Ochieng", "title": "Master Barber", "experience": "12 years", "specialty": "Precision cuts & scalp care"},
        {"name": "Samuel Ndungu", "title": "Barber Specialist", "experience": "8 years", "specialty": "Family services & kids cuts"},
        {"name": "Michael Wanjiku", "title": "Junior Master Barber", "experience": "5 years", "specialty": "Contemporary styles & grooming"}
    ]
    
    cols = st.columns(len(team_members))
    for i, member in enumerate(team_members):
        with cols[i]:
            st.markdown(f"""
            <div class="feature-card">
                <h4 style="color: #1e3c72; margin-bottom: 0.5rem;">👨‍💼 {member['name']}</h4>
                <p style="color: #4a90e2; font-weight: 500; margin: 0.5rem 0;"><strong>{member['title']}</strong></p>
                <p style="color: #666; margin: 0.5rem 0;">Experience: {member['experience']}</p>
                <p style="color: #555; font-style: italic; margin: 0;"><em>{member['specialty']}</em></p>
            </div>
            """, unsafe_allow_html=True)

elif page == '📸 Gallery':
    st.markdown('<h1 class="main-header">Our Gallery</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="hero-section" style="padding: 2rem;">
        <h3 style="margin-bottom: 1rem;">Witness the Art of Precision</h3>
        <p style="font-size: 1.1rem; line-height: 1.6; max-width: 600px; margin: 0 auto;">
        Every cut tells a story of craftsmanship, precision, and dedication to excellence. 
        Browse our portfolio showcasing the artistry that defines Classic Executive Barber Shop.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    gallery_categories = ["✂️ Executive Cuts", "🪒 Traditional Shaves", "🧔 Beard Artistry", "👦 Kids Styling", "🏪 Our Space"]
    selected_category = st.selectbox("📂 Browse Gallery Categories:", gallery_categories)
    
    if selected_category == "✂️ Executive Cuts":
        st.markdown('<h3 class="sub-header">Executive Haircut Portfolio</h3>', unsafe_allow_html=True)
        st.markdown("""
        <div class="service-card">
        <p style="line-height: 1.8; color: #555;">
        Our signature executive cuts demonstrate precision, sophistication, and attention to detail. 
        Each style is carefully crafted to complement the client's features, profession, and personal aesthetic.
        </p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        gallery_items = [
            ("🖼️ Classic Business Cut", "Timeless elegance for the professional"),
            ("🖼️ Modern Executive Style", "Contemporary sophistication"),
            ("🖼️ Precision Fade Cut", "Technical excellence in styling"),
            ("🖼️ Textured Professional", "Modern texture with classic appeal"),
            ("🖼️ Distinguished Gentleman", "Refined styling for mature clients"),
            ("🖼️ Corporate Executive", "Power styling for business leaders")
        ]
        
        for i, (title, description) in enumerate(gallery_items):
            with [col1, col2, col3][i % 3]:
                st.markdown(f"""
                <div class="feature-card">
                    <h4 style="color: #1e3c72; margin-bottom: 1rem;">{title}</h4>
                    <p style="color: #666; font-style: italic;">{description}</p>
                </div>
                """, unsafe_allow_html=True)
    
    elif selected_category == "🪒 Traditional Shaves":
        st.markdown('<h3 class="sub-header">Traditional Wet Shave Experience</h3>', unsafe_allow_html=True)
        st.markdown("""
        <div class="service-card">
        <p style="line-height: 1.8; color: #555;">
        Experience the luxury and precision of traditional wet shaving with hot towels, premium lathers, 
        and expertly honed razors for the smoothest, most comfortable shave possible.
        </p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        shave_items = [
            ("🖼️ Hot Towel Preparation", "Relaxing steam treatment"),
            ("🖼️ Premium Lather Application", "Rich, protective foam"),
            ("🖼️ Precision Razor Work", "Expert blade technique"),
            ("🖼️ Aftercare Treatment", "Soothing post-shave care"),
            ("🖼️ Complete Transformation", "Before and after results"),
            ("🖼️ Luxury Experience", "Traditional barbering at its finest")
        ]
        
        for i, (title, description) in enumerate(shave_items):
            with [col1, col2, col3][i % 3]:
                st.markdown(f"""
                <div class="feature-card">
                    <h4 style="color: #1e3c72; margin-bottom: 1rem;">{title}</h4>
                    <p style="color: #666; font-style: italic;">{description}</p>
                </div>
                """, unsafe_allow_html=True)
    
    elif selected_category == "🧔 Beard Artistry":
        st.markdown('<h3 class="sub-header">Beard Styling & Grooming</h3>', unsafe_allow_html=True)
        st.markdown("""
        <div class="service-card">
        <p style="line-height: 1.8; color: #555;">
        From full beard maintenance to precise styling, our artists create the perfect beard 
        that complements your face shape and enhances your overall appearance.
        </p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        beard_items = [
            ("🖼️ Full Beard Sculpting", "Complete beard transformation"),
            ("🖼️ Precision Goatee", "Defined and sophisticated"),
            ("🖼️ Mustache Artistry", "Classic and contemporary styles"),
            ("🖼️ Beard Line Definition", "Clean, sharp lines"),
            ("🖼️ Texture & Volume", "Natural, well-groomed appearance"),
            ("🖼️ Maintenance Styling", "Professional upkeep")
        ]
        
        for i, (title, description) in enumerate(beard_items):
            with [col1, col2, col3][i % 3]:
                st.markdown(f"""
                <div class="feature-card">
                    <h4 style="color: #1e3c72; margin-bottom: 1rem;">{title}</h4>
                    <p style="color: #666; font-style: italic;">{description}</p>
                </div>
                """, unsafe_allow_html=True)
    
    elif selected_category == "👦 Kids Styling":
        st.markdown('<h3 class="sub-header">Children\'s Grooming Services</h3>', unsafe_allow_html=True)
        st.markdown("""
        <div class="service-card">
        <p style="line-height: 1.8; color: #555;">
        We make haircuts fun and comfortable for children with patient, gentle service 
        and age-appropriate styling that keeps young clients looking sharp and feeling confident.
        </p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        kids_items = [
            ("🖼️ First Haircut Experience", "Gentle introduction to grooming"),
            ("🖼️ School-Ready Styles", "Neat and practical cuts"),
            ("🖼️ Trendy Kids Cuts", "Age-appropriate modern styles"),
            ("🖼️ Patient Care", "Comfortable, stress-free service"),
            ("🖼️ Family Experience", "Parents and children together"),
            ("🖼️ Fun Atmosphere", "Making grooming enjoyable")
        ]
        
        for i, (title, description) in enumerate(kids_items):
            with [col1, col2, col3][i % 3]:
                st.markdown(f"""
                <div class="feature-card">
                    <h4 style="color: #1e3c72; margin-bottom: 1rem;">{title}</h4>
                    <p style="color: #666; font-style: italic;">{description}</p>
                </div>
                """, unsafe_allow_html=True)
    
    elif selected_category == "🏪 Our Space":
        st.markdown('<h3 class="sub-header">Classic Interior & Atmosphere</h3>', unsafe_allow_html=True)
        st.markdown("""
        <div class="service-card">
        <p style="line-height: 1.8; color: #555;">
        Step into our elegantly designed space featuring vintage barber chairs, classic décor, 
        and a warm, welcoming atmosphere that embodies traditional barbering excellence.
        </p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        space_items = [
            ("🖼️ Classic Barber Stations", "Vintage elegance meets modern comfort"),
            ("🖼️ Premium Equipment", "State-of-the-art tools and instruments"),
            ("🖼️ Relaxing Atmosphere", "Sophisticated, calming environment"),
            ("🖼️ Reception Area", "Welcoming first impressions"),
            ("🖼️ Traditional Décor", "Timeless barbering heritage"),
            ("🖼️ Comfort & Luxury", "Premium client experience")
        ]
        
        for i, (title, description) in enumerate(space_items):
            with [col1, col2, col3][i % 3]:
                st.markdown(f"""
                <div class="feature-card">
                    <h4 style="color: #1e3c72; margin-bottom: 1rem;">{title}</h4>
                    <p style="color: #666; font-style: italic;">{description}</p>
                </div>
                """, unsafe_allow_html=True)
    
    # Customer Testimonials
    st.markdown('<h3 class="sub-header">💬 Client Testimonials</h3>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    testimonials = [
        {
            "text": "Outstanding service and attention to detail. James gave me the perfect cut for my wedding day. Absolutely recommend this place!",
            "author": "David K., CEO"
        },
        {
            "text": "Been coming here for 5 years. Consistently excellent service, professional atmosphere, and skilled barbers who understand what I need.",
            "author": "Michael O., Lawyer"
        },
        {
            "text": "Perfect place for a professional cut. The team is patient with my son and the results are always impressive. Five stars!",
            "author": "Sarah M., Parent"
        }
    ]
    
    for i, testimonial in enumerate(testimonials):
        with [col1, col2, col3][i]:
            st.markdown(f"""
            <div class="testimonial">
                <p style="font-style: italic; margin-bottom: 1rem; line-height: 1.6;">"{testimonial['text']}"</p>
                <p style="text-align: right; font-weight: 500; color: #1e3c72; margin: 0;">— {testimonial['author']}</p>
            </div>
            """, unsafe_allow_html=True)

elif page == '📞 Contact':
    st.markdown('<h1 class="main-header">Contact Us</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div class="contact-info">
            <h3>📍 Visit Our Location</h3>
            <p style="font-size: 1.1rem; margin: 1rem 0;"><strong>Classic Executive Barber Shop</strong></p>
            <p style="margin: 0.5rem 0;">📍 Kimathi Street, City Centre<br>Nairobi, Kenya</p>
            
            <h3 style="margin-top: 2rem;">📞 Contact Information</h3>
            <p style="margin: 0.5rem 0;">📱 Main Line: +254 712 345 678<br>📱 WhatsApp: +254 798 765 432</p>
            
            <h3 style="margin-top: 2rem;">📧 Email</h3>
            <p style="margin: 0.5rem 0;">✉️ info@classicexecutivebarber.com<br>✉️ bookings@classicexecutivebarber.com</p>
            
            <h3 style="margin-top: 2rem;">🕐 Operating Hours</h3>
            <div style="text-align: left; margin: 1rem 0;">
                <p style="margin: 0.3rem 0;"><strong>Monday - Friday:</strong> 8:00 AM - 8:00 PM</p>
                <p style="margin: 0.3rem 0;"><strong>Saturday:</strong> 8:00 AM - 9:00 PM</p>
                <p style="margin: 0.3rem 0;"><strong>Sunday:</strong> 10:00 AM - 6:00 PM</p>
            </div>
            
            <h3 style="margin-top: 2rem;">🌐 Social Media</h3>
            <p style="margin: 0.5rem 0;">📘 Facebook: Classic Executive Barber<br>📷 Instagram: @classicexecutivebarber<br>🐦 Twitter: @ClassicBarberKE</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown('<h3 class="sub-header">💌 Send Us a Message</h3>', unsafe_allow_html=True)
        
        st.markdown('<div class="booking-form">', unsafe_allow_html=True)
        
        with st.form("contact_form"):
            contact_name = st.text_input("👤 Your Name*", placeholder="Enter your full name")
            contact_email = st.text_input("📧 Your Email*", placeholder="your.email@example.com")
            contact_phone = st.text_input("📱 Your Phone", placeholder="+254 7XX XXX XXX")
            message_type = st.selectbox("📋 Inquiry Type", 
                                      ["General Information", "Booking Assistance", "Service Question", 
                                       "Feedback", "Corporate Services", "Other"])
            message = st.text_area("💬 Your Message*", 
                                 placeholder="Please share your questions, feedback, or how we can assist you...",
                                 height=120)
            
            submitted = st.form_submit_button("📤 SEND MESSAGE", type="primary", use_container_width=True)
            
            if submitted:
                if contact_name and contact_email and message:
                    with st.spinner("Sending your message..."):
                        time.sleep(1.5)
                    st.success("""
                    ✅ **Message Sent Successfully!**
                    
                    Thank you for contacting Classic Executive Barber Shop. 
                    Our team will respond to your inquiry within 24 hours.
                    
                    📱 For urgent matters, please call +254 712 345 678
                    """)
                else:
                    st.error("⚠️ Please fill in all required fields marked with *")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Additional Information
        st.markdown("""
        <div class="service-card" style="margin-top: 2rem;">
            <h4 style="color: #1e3c72; margin-bottom: 1rem;">🚨 Emergency Contact</h4>
            <p style="color: #555; line-height: 1.6;">
            For urgent matters outside business hours or existing client emergencies:
            </p>
            <p style="color: #1e3c72; font-weight: 500;">📱 Emergency Line: +254 700 123 456</p>
            <p style="color: #666; font-size: 0.9rem; font-style: italic;">
            *Available for existing clients with special scheduling needs
            </p>
        </div>
        
        <div class="service-card" style="margin-top: 1rem;">
            <h4 style="color: #1e3c72; margin-bottom: 1rem;">🚗 Parking Information</h4>
            <p style="color: #555; line-height: 1.6;">
            Complimentary parking available for all clients. Street parking and nearby 
            commercial parking facilities also accessible.
            </p>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <h3 style="font-family: 'Playfair Display', serif; margin-bottom: 1rem;">✂️ CLASSIC EXECUTIVE BARBER SHOP</h3>
    <p style="font-size: 1.1rem; opacity: 0.9; margin: 0.5rem 0;">"Where Style Meets Tradition"</p>
    <p style="opacity: 0.8; margin: 1rem 0;">📍 Kimathi Street, Nairobi | 📱 +254 712 345 678 | ✉️ info@classicexecutivebarber.com</p>
    <div style="margin: 1.5rem 0; opacity: 0.7;">
        <p style="margin: 0.3rem 0;">Monday - Friday: 8:00 AM - 8:00 PM | Saturday: 8:00 AM - 9:00 PM | Sunday: 10:00 AM - 6:00 PM</p>
    </div>
    <p style="font-size: 0.9rem; opacity: 0.6; margin: 0;">© 2025 Classic Executive Barber Shop. All rights reserved. | Crafted with excellence in Nairobi, Kenya</p>
</div>
""", unsafe_allow_html=True)