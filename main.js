const { app, BrowserWindow, Menu } = require('electron');
const path = require('path');

function createWindow() {
    const win = new BrowserWindow({
        width: 950,
        height: 680,
        resizable: true,
        icon: path.join(__dirname, 'assets/goku1.png'), // Using goku1 as app icon for now
        webPreferences: {
            nodeIntegration: false,
            contextIsolation: true
        }
    });

    // Remove the default menu bar for a cleaner look
    Menu.setApplicationMenu(null);

    win.loadFile('index.html');
}

app.whenReady().then(() => {
    createWindow();

    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) {
            createWindow();
        }
    });
});

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});
