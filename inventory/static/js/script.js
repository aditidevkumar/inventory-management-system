document.addEventListener("DOMContentLoaded", function() {
    document.querySelector('.animated').style.opacity = 0;
    setTimeout(() => {
        document.querySelector('.animated').style.opacity = 1;
        document.querySelector('.animated').style.transition = "opacity 0.5s ease-in-out";
    }, 100);
});