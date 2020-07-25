import React from 'react';
const inject = obj => Comp =>props=><Comp {...obj}{...props} />;
export {inject}