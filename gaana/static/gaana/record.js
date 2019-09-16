/**
 * Created by hp on 8/26/2019.
 */
var record = document.querySelector('#record_btn');
var stop = document.querySelector('#stop_btn');

  if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
     console.log('getUserMedia supported.');
     navigator.mediaDevices.getUserMedia (
        // constraints - only audio needed for this app
        {
           audio: true
        })

        // Success callback
        .then(function(stream) {
          var mediaRecorder = new MediaRecorder(stream);
          record.onclick = function() {
            mediaRecorder.start();
            record.disabled = true;
            stop.disabled = false;
            console.log(mediaRecorder.state);
            console.log("recorder started");
            record.style.background = "red";
            record.style.color = "black";
          }

          var chunks = [];

          mediaRecorder.ondataavailable = function(e) {
            chunks.push(e.data);
          }
          stop.onclick = function() {
            mediaRecorder.stop();
            record.disabled = false;
            stop.disabled = true;
            console.log(mediaRecorder.state);
            console.log("recorder stopped");
            record.style.background = "";
            record.style.color = "";
          }

          mediaRecorder.onstop = function(e) {
            console.log("recorder stopped");
            var audio = document.querySelector('#audio');
            var blob = new Blob(chunks, { 'type' : 'audio/ogg; codecs=opus' });
            chunks = [];
            var audioURL = window.URL.createObjectURL(blob);
            $("#source").attr("src", audioURL);
            $("#audio")[0].load();
            stream.getTracks()[0].stop();

            //CODE TO UPLOAD BLOB DATA TO DJANGO SERVER
            var blob = new Blob(chunks, { 'type' : 'audio/ogg; codecs=opus' });

console.log("start sending binary data...");
var form = new FormData();
form.append('audio', blob);

$.ajax({
    url: 'http://localhost:8000/<your api endpoint>/',
    type: 'POST',
    data: form,
    processData: false,
    contentType: false,
    success: function (data) {
        console.log('response' + JSON.stringify(data));
    },
    error: function () {
       // handle error case here
    }
});
            //
          }
        })

        // Error callback
        .catch(function(err) {
           console.log('The following getUserMedia error occured: ' + err);
        }
     );   } else {
     console.log('getUserMedia not supported on your browser!');   }