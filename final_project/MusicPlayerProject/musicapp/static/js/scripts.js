// static/js/scripts.js

document.addEventListener('DOMContentLoaded', () => {
    const playButtons = document.querySelectorAll('.play-button');
    const audioPlayer = new Audio();

    playButtons.forEach(button => {
        button.addEventListener('click', () => {
            const songUrl = button.getAttribute('data-song');
            
            if (audioPlayer.src !== songUrl) {
                audioPlayer.src = songUrl;
                audioPlayer.play();
            } else {
                if (audioPlayer.paused) {
                    audioPlayer.play();
                } else {
                    audioPlayer.pause();
                }
            }
        });
    });
});


// static/js/scripts.js

document.addEventListener('DOMContentLoaded', () => {
    // Fetch Spotify track data
    fetch('/api/get_spotify_track/spotify_track_id/')
        .then(response => response.json())
        .then(data => {
            // Use data to display track information in your UI
        });

    // Fetch SoundCloud track data
    fetch('/api/get_soundcloud_track/soundcloud_track_id/')
        .then(response => response.json())
        .then(data => {
            // Use data to display track information in your UI
        });
});

// static/js/scripts.js

document.addEventListener('DOMContentLoaded', () => {
    const playButton = document.querySelector('.play-button');
    const pauseButton = document.querySelector('.pause-button');
    const stopButton = document.querySelector('.stop-button');

    playButton.addEventListener('click', () => {
        const songId = /* Get the song ID */;
        fetch(`/api/play/${songId}/`)
            .then(response => response.json())
            .then(data => {
                // Handle the response
            });
    });

    pauseButton.addEventListener('click', () => {
        fetch('/api/pause/')
            .then(response => response.json())
            .then(data => {
                // Handle the response
            });
    });

    stopButton.addEventListener('click', () => {
        fetch('/api/stop/')
            .then(response => response.json())
            .then(data => {
                // Handle the response
            });
    });
});
