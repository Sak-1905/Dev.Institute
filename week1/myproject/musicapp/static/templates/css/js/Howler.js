document.addEventListener('DOMContentLoaded', function () {
    const sound = new Howl({
        src: ['path/to/audio.mp3'],
        // Add more options as needed
    });

    const playButton = document.getElementById('play-button');
    const pauseButton = document.getElementById('pause-button');
    const stopButton = document.getElementById('stop-button');

    playButton.addEventListener('click', function () {
        sound.play();
    });

    pauseButton.addEventListener('click', function () {
        sound.pause();
    });

    stopButton.addEventListener('click', function () {
        sound.stop();
    });
});
