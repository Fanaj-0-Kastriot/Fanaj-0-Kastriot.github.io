const videoContainer = document.querySelector('.video-container');

window.addEventListener('wheel', function(event) {
  if (event.deltaY > 0) { 
    videoContainer.style.transition = 'height 0.5s ease';
    videoContainer.style.height = '0';
    setTimeout(function() {
      window.location.href = 'test.html';
    }, 500);
  } else {
    videoContainer.style.transition = 'height 0.5s ease';
    videoContainer.style.height = 'calc(100vh - 70px)';
    setTimeout(function() {
      document.querySelector('.image').style.display = 'none';
      document.querySelector('.video').style.display = 'block';
    }, 500);
  }
});