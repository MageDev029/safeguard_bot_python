'use client';  

import React from 'react';  
import TelegramLoginButton from 'react-telegram-login';  

// Define a type for the Telegram response  
interface TelegramResponse {  
  id: number;           // User ID  
  first_name: string;   // User's first name  
  last_name?: string;   // User's last name (optional)  
  username?: string;    // User's username (optional)  
  photo_url?: string;   // User's photo URL (optional)  
  auth_date: number;    // Authentication date (timestamp)  
  hash: string;         // Hash for verification  
}  

const QrLogin: React.FC = () => {  
  const handleTelegramResponse = (response: TelegramResponse) => {  
    console.log(response);  
    
    // Add your verification logic here  
    // Example: Verify the response hash to ensure data integrity  
  };  

  return (  
    <div>  
      <TelegramLoginButton   
        dataOnauth={handleTelegramResponse}   
        botName="Wh_SafeguardUXRobot"  // Ensure this is your bot's correct username (without @)  
        buttonSize={50}                // Optional: adjust button size  
        cornerRadius={20}              // Optional: adjust corner radius  
        theme="light"                  // Optional: choose theme (light or dark)  
      />  
    </div>  
  );  
};  

export default QrLogin;  