const audioInput = document.getElementById('audioInput');
const audioPlayer = document.getElementById('audioPlayer');
const pitchSlider = document.getElementById('pitch');
const rateSlider = document.getElementById('rate');
const volumeSlider = document.getElementById('volume');
const resetBtn = document.getElementById('resetBtn');

// Audio context e nodi
let audioContext;
let sourceNode;
let gainNode;

audioInput.addEventListener('change', (e) => {
  const file = e.target.files[0];
  if (!file) return;
  const url = URL.createObjectURL(file);
  audioPlayer.src = url;
});

audioPlayer.addEventListener('play', () => {
  audioContext = new (window.AudioContext || window.webkitAudioContext)();
  sourceNode = audioContext.createMediaElementSource(audioPlayer);
  gainNode = audioContext.createGain();

  sourceNode.connect(gainNode);
  gainNode.connect(audioContext.destination);

  applySettings();
});

pitchSlider.addEventListener('input', () => {
  // Pitch (simulato via playbackRate)
  audioPlayer.playbackRate = pitchSlider.value;
});

rateSlider.addEventListener('input', () => {
  audioPlayer.playbackRate = rateSlider.value;
});

volumeSlider.addEventListener('input', () => {
  if (gainNode) {
    gainNode.gain.value = volumeSlider.value;
  }
});

resetBtn.addEventListener('click', () => {
  pitchSlider.value = 1;
  rateSlider.value = 1;
  volumeSlider.value = 1;
  audioPlayer.playbackRate = 1;
  if (gainNode) gainNode.gain.value = 1;
});

function applySettings() {
  audioPlayer.playbackRate = rateSlider.value;
  if (gainNode) gainNode.gain.value = volumeSlider.value;
}

