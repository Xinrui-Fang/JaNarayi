music_name = "./static/segmentFile/chunk0.wav?cb=" + new Date().getTime();
console.log(music_name.slice(0, music_name.indexOf("?")));

//music_name = "{{ url_for('static', filename = '../segmentFile/chunk0.wav') }}"
let play_btn = document.querySelector("#play");
let prev_btn = document.querySelector("#pre");
let next_btn = document.querySelector("#next");
let range = document.querySelector("#range");
let play_img = document.querySelector("#play_img")
let total_time = 0;
let currentTime = 0;
let isPlaying = false;
let song = new Audio();
let chunk = 0;
window.onload = playSong;

function playSong(){
    song.src = music_name;
    song.load();
    loadXMLDoc(music_name.slice(0, music_name.indexOf("?")));
    //console.log(song)
    
    
    play_btn.addEventListener('click',function(){
        if(!isPlaying){
            //song.load();
            song.play();
            isPlaying = true;
            total_time = song.duration;
            range.max = total_time;
            play_img.src = "./static/pause.png";
        }else{
            song.pause();
            isPlaying = false;
            play_img.src = "./static/play.png";
        }
       song.addEventListener('ended',function(){
            song.currentTime = 0
            song.pause();
            isPlaying = false;
            range.value = 0;
            play_img.src = "./static/play.png";
        })
        song.addEventListener('timeupdate',function(){
            range.value = song.currentTime;
        })
        range.addEventListener('change',function(){
            song.currentTime = range.value;
        })
       
    })

    next_btn.addEventListener('click',function(){
        chunk += 1;
        music_name = "./static/segmentFile/chunk"+chunk.toString()+ ".wav";
       
        loadXMLDoc(music_name);
        song.src = music_name;
        
        play_img.src = "./static/play.png";
        //console.log(song);

    
    })

    prev_btn.addEventListener('click',function(){
        chunk -= 1;
        if (chunk>=0){
            music_name = "./static/segmentFile/chunk"+chunk.toString()+ ".wav";
            
            loadXMLDoc(music_name);
            song.src = music_name;
            
            play_img.src = "./static/play.png";
            //console.log(song);


        }
    })
}

function loadXMLDoc(filename){
    $.getJSON($SCRIPT_ROOT + '/_add_numbers', {
        a: filename
      }, function(data) {
        $("#title").text(data.result);
      });
      return false;
}
    
     
   

