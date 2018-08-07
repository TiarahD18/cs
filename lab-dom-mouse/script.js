const button =document.querySelector('button');
button.addEventListener('mouseover', () =>{
  button.innerHTML = "don't click";
  button.classList.add('danger');
});

button.addEventListener('mousemove', () => {
  size = size + 1;
  button.style.width = size + '1px';
  button.style.height = size + '1px';
});
