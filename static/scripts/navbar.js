// Add active state to navigation links
window.addEventListener('scroll', function () {
    const sections = document.querySelectorAll('section[id]');
    const navLinks = navLinksWrapper.querySelectorAll('a');
    let current = '';
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (scrollY >= sectionTop - 200) {
            current = section.getAttribute('id');
        }
    });
    
    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href').substring(1) === current) {
            link.classList.add('active');
        }
    });
});

// Language selector functionality
const languageSelector = document.querySelector('.language-selector');
const languageDropdown = document.getElementById('languageDropdown');
const selectedFlag = document.getElementById('selectedFlag');
const selectedLanguage = document.getElementById('selectedLanguage');
const languageOptions = document.querySelectorAll('.language-option');
const hamburgerToggle = document.querySelector('.hamburger-icon');
const hamburgerIcon = hamburgerToggle.querySelector('.bi');
const navLinksWrapper = document.querySelector('.nav-links');
const selectedIcon = document.querySelector('.selectedFlag-icon');
const languageInput = document.querySelector('.language-input');
// Toggle hamburger menu
hamburgerToggle.addEventListener('click', function () {
    console.log('Hamburger menu toggled');
    hamburgerIcon.classList.toggle('bi-list');
    hamburgerIcon.classList.toggle('bi-x-lg');
    navLinksWrapper.classList.toggle('active');
    languageSelector.classList.toggle('Active');
    console.log(languageSelector);

});

// Toggle dropdown
languageSelector.addEventListener('click', function (e) {
    e.stopPropagation();
    languageSelector.classList.toggle('active');
    languageDropdown.classList.toggle('active');
});

// Handle language selection
//just extrcact the chosen language and print it to the console
languageOptions.forEach(option => {
    option.addEventListener('click', function (e) {
        e.stopPropagation();

        // Remove selected class from all options
        languageOptions.forEach(opt => opt.classList.remove('selected'));

        // Add selected class to clicked option
        this.classList.add('selected');

        // Update selected language display
        const lang = this.dataset.lang;
        const flag = this.dataset.flag;
        const text = this.querySelector('.language-text').textContent;

        selectedFlag.className = `flag ${flag}`;
        console.log(lang);
        selectedLanguage.textContent = text;
        new_class = ''
        switch (lang) {
            case 'en':
                new_class = 'fi-gb';
                break;
            case 'fr':
                new_class = 'fi-fr';
                break;
            case 'ar':
                new_class = 'fi-dz';
                break;
            default:
                new_class = 'fi-gb'; // Default to English flag
                break;
        }
        selectedIcon.className = `fi ${new_class} selectedFlag-icon`;
            

        // Close dropdown
        languageSelector.classList.remove('active');
        languageDropdown.classList.remove('active');

        //language switching logic
        //we should first set the value of the hidden input field
        languageInput.value = lang;
        //we should submit the form and send the post request to the server
        //
        console.log(`Language changed to: ${lang}`);
        languageSelector.submit();



        // Example: Change document language attribute
        document.documentElement.lang = lang;

        // Example: Apply RTL for Arabic
        if (lang === 'ar') {
            document.body.style.direction = 'rtl';
        } else {
            document.body.style.direction = 'ltr';
        }
    });
});

// Close dropdown when clicking outside
document.addEventListener('click', function () {
    languageSelector.classList.remove('active');
    languageDropdown.classList.remove('active');
});

// Prevent dropdown from closing when clicking inside it
languageDropdown.addEventListener('click', function (e) {
    e.stopPropagation();
});