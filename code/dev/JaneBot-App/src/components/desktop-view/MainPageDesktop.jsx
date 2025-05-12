/* 
  Main Page - Desktop View
*/

/* 
  TODO ----------

  - Add the like button again! It was removed due to it causing bugs
*/

// Main Imports
import { useState, useEffect } from 'react';

// Style Imports
import './../../styles/desktop-view/main-page-1.css';

// Image imports
import ChibiRobin from "./../../images/chibi_robin.jpeg"
import RJIcon from "./../../images/ashleybop.gif"

/* 
  ################## Main Configuration ################## 
*/

function MainPageDesktop() {
  const [darkMode, setDarkMode] = useState(false);
  const [likeCount, setLikeCount] = useState(0);
  const [isLiked, setIsLiked] = useState(false);

  useEffect(() => {
    if (darkMode) {
      document.body.classList.add('dark-theme');
    } else {
      document.body.classList.remove('dark-theme');
    }
  }, [darkMode]);

  const toggleTheme = () => {
    setDarkMode(!darkMode);
  };

  // Toggle function that combines both
  const toggleLeftBox = () => {
    const leftBox = document.querySelector('.left-box-container');
    if (leftBox) {
      // Check current width and toggle
      if (leftBox.style.width === '0px' || leftBox.style.width === '') {
        leftBox.style.width = '100vw';
        // Optionally change the button icon
        const menuIcon = document.querySelector('.menu-icon');
        if (menuIcon) menuIcon.textContent = '×';
      } else {
        leftBox.style.width = '0';
        // Optionally change the button icon
        const menuIcon = document.querySelector('.menu-icon');
        if (menuIcon) menuIcon.textContent = '☰';
      }
    }
  };

  return (
    <div className="main-page-desktop-container">
      <div className="left-box-container">

        <button 
          className={`theme-toggle ${darkMode ? 'dark' : 'light'}`}
          onClick={toggleTheme}
          aria-label="Toggle dark/light mode"
        >
          {darkMode ? '☀️' : '🌙'}
        </button>

        <div className="reveal-left-box-container">
          <button 
            className="toggle-menu-button"
            onClick={toggleLeftBox}
            aria-label="Toggle menu"
          >
            <span className="menu-icon">☰</span>
          </button>
        </div>

        <div className="left-box-top-image-container">
          <div className="left-box-top-image">
            <img src={ChibiRobin}/>
          </div>
        </div>

        <div className="left-box-title-block">
          <div className='devlog-title-block'>DevLog Contents</div>
          {/* 
              TODO ----------

              Include hyperlinks to certain DevLogs
          */}
          <div className='devlog-title-underline-container'>
            <div className='devlog-title-underline' />
          </div>
        </div>

      </div>

      <div className="full-page-divider" />

      <div className="right-box-container">
        {/* ##### POST BOX #####  */}
        <div className="post-box-container">
          <div className="post-box">
            <div className="inside-post-box">
              {/* #### TOP BOX ### */}
              <div className="post-box-top-box">
                <div className="post-box-user-icon">
                  <img src={RJIcon} />
                </div>

                <div className="post-box-user-icon-gap">
                </div>

                <div className="post-box-user-name-box">
                  <div className="post-box-name-box-container">
                    <div className="post-box-name-box-username">
                      <div>
                        Smoodeazy
                      </div>
                    </div>
                    <div className="post-box-name-box-username-two">
                      <div>
                        @bestfullstackdeveloper
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              {/* #### TOP BOX ### */}

              {/* #### TEXT BOX #### */}
              <div className="post-box-text-box">

                First live deployment of the blog!
                <br />
                There's a lot of bugs but I'll be sure to fix those soon. Please stay tuned!

                <br />
                <span className="hashtag">
                  #fixdembugs
                </span>
              </div>
              {/* #### TEXT BOX #### */}

              {/* #### TIME STAMP BOX #### */}
              <div className="timestamp-container">
                19:38PM 。 2025-04-20
              </div>
              {/* #### TIME STAMP BOX #### */}
            </div>
          </div>
        </div> 
        {/* ##### POST BOX #####  */}

        {/* ##### POST BOX #####  */}
        <div className="post-box-container">
          <div className="post-box">
            <div className="inside-post-box">
              {/* #### TOP BOX ### */}
              <div className="post-box-top-box">
                <div className="post-box-user-icon">
                  <img src={RJIcon} />
                </div>

                <div className="post-box-user-icon-gap">
                </div>

                <div className="post-box-user-name-box">
                  <div className="post-box-name-box-container">
                    <div className="post-box-name-box-username">
                      <div>
                        Smoodeazy
                      </div>
                    </div>
                    <div className="post-box-name-box-username-two">
                      <div>
                        @bestfullstackdeveloper
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              {/* #### TOP BOX ### */}

              {/* #### TEXT BOX #### */}
              <div className="post-box-text-box">
                Looks like the blog posts are working just fine :/
                <br />
                Tbh, decent progress has been made. But I'll play a few Hoyoverse games to prevent burn out.
                <br />
                <span className="hashtag">
                  #dontlose5050s
                </span>
              </div>
              {/* #### TEXT BOX #### */}

              {/* #### TIME STAMP BOX #### */}
              <div className="timestamp-container">
                21:31PM 。 2025-04-18
              </div>
              {/* #### TIME STAMP BOX #### */}
            </div>
          </div>
        </div> 
        {/* ##### POST BOX #####  */}
      </div>
    </div>
  )
}

export default MainPageDesktop;
