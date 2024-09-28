// Check if the URL contains the access token from Discord
window.onload = function() {
    // Get the URL hash
    const hash = window.location.hash;

    // Check if there's an access token in the hash
    if (hash) {
        const params = new URLSearchParams(hash.substring(1)); // Remove the "#" from the hash

        const accessToken = params.get('access_token');
        if (accessToken) {
            console.log('Access Token:', accessToken);
            // You can now use the access token to make API requests to Discord
            // For example, fetch user data
            fetchUserData(accessToken);
        } else {
            console.error('Access token not found in the URL hash.');
        }
    }
};

// Function to fetch user data from Discord
function fetchUserData(token) {
    fetch('https://discord.com/api/v10/users/@me', {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${token}`
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        console.log('User Data:', data);
        // Handle user data here (e.g., display on the page)
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });
}
