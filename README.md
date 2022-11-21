
<h1 align="center">
  <br>
  <a href="https://w7.pngwing.com/pngs/657/861/png-transparent-bloomberg-terminal-business-bloomberg-government-organization-business-text-people-logo.png" alt="Farmproject" width="200"></a>
  <br>
  Farmproject Bloomberg
  <br>
</h1>

<p align="center">
  <a href="https://badge.fury.io/js/electron-markdownify">
    <img src="https://badge.fury.io/js/electron-markdownify.svg"
         alt="Gitter">
  </a>
</p>

<p align="center">
  <a href="#how-to-use">How To Use</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a>
</p>

<p align="center">
<img src="https://media1.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif">
</p>
## Key Features
* Cross platform
  - Windows, macOS and Linux ready.
  - Modernized UI, easy to use

## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com) and [Node.js](https://nodejs.org/en/download/) (which comes with [npm](http://npmjs.com)) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/hackaTUM-2022/farmproject.git

# Go into the backend repository
$ cd backend/

# Install the other requirements 
$ pip install -r requirements.txt
```
> **Note**
> Use ifconfig in the command line  to get your IP.<br/>
> You also need to have MongoDB installed. Please Visit their official website for that [see this guide](https://www.mongodb.com/)
```bash
# Run the FastAPI Server and replace the host_ip with your IP
$ uvicorn main:app  --reload --host 0.0.0.0 --port 8000
# Client side need the use http:[host_ip]:8000/api/todo

# Go and clone the frontend repository named dashboard
$ https://github.com/hackaTUM-2022/dashboard.git

# Install dependencies
$ npm install

# Run the app
$ npm start
```

> **Note**
> If you're using Linux Bash for Windows, [see this guide](https://www.howtogeek.com/261575/how-to-run-graphical-linux-desktop-applications-from-windows-10s-bash-shell/) or use `node` from the command prompt.
> If you are not familiar with npm, [see this guide](https://linuxconfig.org/install-npm-on-linux)

## Credits

This software uses the following open source packages:

- [Node.js](https://nodejs.org/)

## License

Copyright 2022 Bloomberg hackaTUM-2022

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
---



