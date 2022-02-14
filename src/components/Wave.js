import React, { Component } from 'react';

class MySvg extends Component {
  render() {
    return <BasicSvg />;
  }
}

const BasicSvg = () =>
  <svg xmlns="http://www.w3.org/2000/svg" 
  version="1.1" 
  width="1440" 
  height="560" 
  preserveAspectRatio="none" 
  viewBox="0 0 1440 560">
  <g mask="url(&quot;#SvgjsMask1015&quot;)" fill="none">
  <rect width="1440" height="560" x="0" y="0" fill="#0e2a47"></rect>
  <path d="M 0,258 C 57.6,219.2 172.8,67.4 288,64 C 403.2,60.6 460.8,246.6 576,241 C 691.2,235.4 748.8,51.4 864,36 C 979.2,20.6 1036.8,148.6 1152,164 C 1267.2,179.4 1382.4,123.2 1440,113L1440 560L0 560z" fill="#184a7e"></path>
  <path d="M 0,380 C 96,406 288,515.4 480,510 C 672,504.6 768,360 960,353 C 1152,346 1344,450.6 1440,475L1440 560L0 560z" fill="#2264ab"></path>
  </g>
  <defs>
  <mask id="SvgjsMask1015">
  <rect width="1440" height="560" fill="#ffffff"></rect>
  </mask>
  </defs>
  </svg>

export default MySvg;
