// Defining the functions
async function fetchMenu() {
    const response = await fetch('assets/html/menu.html');
    const html = await response.text();
    //console.log(`html = ${html}`);
    //console.log('Menu replaced with javascript.')
    document.getElementById('menu').innerHTML = html;
}

// Also fill in the footer
async function fetchFooter() {
    const response = await fetch('assets/html/footer.html');
    const html = await response.text();
    //console.log(`html = ${html}`);
    //console.log('Footer replaced with javascript.')
    document.getElementById('footer').innerHTML = html;
}

// Calling the functions
fetchMenu().catch(error => {
    console.error(error);
});

fetchFooter().catch(error => {
    console.error(error);
});