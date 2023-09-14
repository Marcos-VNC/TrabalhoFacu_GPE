const resizableColumns = document.querySelectorAll('.resizable');
let startX;
let startWidth;
resizableColumns.forEach(column => {
    column.style.position = 'relative';

    const resizer = document.createElement('div');
    resizer.classList.add('resizer');
    resizer.style.height = '100%';
    resizer.style.width = '5px';
    resizer.style.position = 'absolute';
    resizer.style.right = '0';
    resizer.style.top = '0';
    resizer.style.cursor = 'col-resize';
    column.appendChild(resizer);

    resizer.addEventListener('mousedown', (e) => {
        startX = e.pageX;
        startWidth = parseFloat(getComputedStyle(column, null).getPropertyValue('width').replace('px', ''));
    });

    document.addEventListener('mousemove', (e) => {
        if (startX) {
            const newWidth = startWidth + (e.pageX - startX);
            column.style.width = newWidth + 'px';
        }
    });

    document.addEventListener('mouseup', () => {
        startX = undefined;
    });
});
