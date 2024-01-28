(function () {
    // Get all the video parts
    let video_parts = document.getElementsByClassName("video_part");
    // Define a function to toggle the visibility of a video part
    function open_video_part(origin) {
        // Get the parent element of the clicked element
        let parent = origin.parentElement;
        // Get the next sibling element of the parent, which is the video file
        let video_file = parent.nextElementSibling;
        // Check if the video file is hidden or not
        if (video_file.style.display === 'none') {
            // If hidden, show it
            video_file.style.display = 'block';
        } else {
            // If not hidden, hide it
            video_file.style.display = 'none';
        }
    }
    // Loop over all the video parts and hide them by default
    for (let video_part of video_parts) {
        video_part.style.display = 'none';
    }
    // Assign the toggle function to the global scope so it can be accessed by the onclick attribute
    window.open_video_part = open_video_part;
})();