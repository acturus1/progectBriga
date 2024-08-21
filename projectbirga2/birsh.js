document.getElementById('themeToggle').addEventListener('click', function() {
    const currentTheme = document.body.className;
    console.log(currentTheme)
    if (currentTheme === 'light-theme') {
        document.body.className = 'dark-theme';
    } else {
        document.body.className = 'light-theme';
    }
});