const canvas = document.getElementById('signature-canvas');
const ctx = canvas.getContext('2d');
const downloadBtn = document.getElementById('download-btn');
const clearBtn = document.getElementById('clear-btn');

let isDrawing = false;

// 设置初始状态
ctx.strokeStyle = '#000';
ctx.lineWidth = 2;
ctx.lineJoin = 'round';
ctx.lineCap = 'round';

// 清除画布
function clearCanvas() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  downloadBtn.disabled = true;
}

// 开始绘制
function startDrawing(e) {
  isDrawing = true;
  draw(e);
}

// 结束绘制
function endDrawing() {
  if (!isDrawing) return;
  isDrawing = false;
  ctx.beginPath();
  downloadBtn.disabled = false;
}

// 绘制过程
function draw(e) {
  if (!isDrawing) return;
  ctx.lineTo(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
  ctx.stroke();
  ctx.beginPath();
  ctx.moveTo(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
}

// 绑定事件
canvas.addEventListener('mousedown', startDrawing);
canvas.addEventListener('mousemove', draw);
canvas.addEventListener('mouseup', endDrawing);
canvas.addEventListener('mouseout', endDrawing);

// 清除按钮事件
clearBtn.addEventListener('click', clearCanvas);

// 下载按钮事件
downloadBtn.addEventListener('click', function() {
  const dataURL = canvas.toDataURL('image/jpg');
  const link = document.createElement('a');
  link.href = dataURL;
  link.download = 'signature.jpg';
  link.click();
});

// 响应移动设备触摸事件
canvas.addEventListener('touchstart', startDrawing);
canvas.addEventListener('touchmove', draw);
canvas.addEventListener('touchend', endDrawing);