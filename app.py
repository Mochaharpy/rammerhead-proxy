document.getElementById('loginBtn').addEventListener('click', function() {
    const clientId = '1289712943277150238'; // Replace with your Discord application client ID
    const redirectUri = 'https://mochaharpy.github.io/rammerhead-proxy/'; // Set this to the URL of your hosted page
    const scope = 'identify email';
    const responseType = 'token';

    const discordOAuthUrl = `https://discord.com/api/oauth2/authorize?client_id=${clientId}&redirect_uri=${encodeURIComponent(redirectUri)}&response_type=${responseType}&scope=${scope}`;
    
    window.location.href = discordOAuthUrl; // Redirecting for OAuth
});

// Function to fetch user data after redirect
window.onload = function() {
    const accessToken = new URLSearchParams(window.location.hash).get('#access_token');
    if (accessToken) {
        fetchUserData(accessToken);
    }
};

function fetchUserData(accessToken) {
    fetch('https://discord.com/api/users/@me', {
        headers: {
            'Authorization': `Bearer ${accessToken}`
        }
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('userInfo').innerHTML = `
            <h2>Hello, ${data.username}!</h2>
            <p>Your email: ${data.email}</p>
            <img src="https://cdn.discordapp.com/avatars/${data.id}/${data.avatar}.png" alt="Avatar" />
        `;
    })
    .catch(error => console.error('Error fetching user data:', error));
}
