    // Intersection Observer for fade-up animations
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, {
        threshold: 0.1
    });

    // Observe all service cards
    document.querySelectorAll('.service-card').forEach(card => {
        card.classList.add('fade-up');
        observer.observe(card);
    });
