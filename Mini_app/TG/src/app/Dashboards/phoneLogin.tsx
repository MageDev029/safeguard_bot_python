'use client';

import React,{useState} from "react";
import Image from "next/image"
import Logo from "@/assets/telegram-svgrepo-com.svg"
import CountrySelect from "@/components/selectCountry"
import PhoneNumberInput from "@/components/phoneNumber"

interface CountryType {
  code: string;
  label: string;
  phone: string;
  suggested?: boolean;
}
export default function PhoneLogin() {
  
  const [selectedCountry, setSelectedCountry] = useState<string | null>(null);
  const [countryPhone, setCountryPhone] = useState<string>('+1 ');
  
  const handleCountryChange = (country: CountryType | null) =>{
      if (country){
        setSelectedCountry(country.label);
        setCountryPhone(`+${country.phone} `);
      } else {
        setCountryPhone("+1 ");
      }
  };
  return (
    <div className="flex flex-col items-center">
       <div>
          <Image 
           src={Logo}
           alt="Telegram Logo"
           className="w-[160px] h-[160px]"
          />
       </div>
       <h1 className="text-[32px] mt-[22px] mb-[24px] font-bold">Sign in to Telegram</h1>
       <p className="text-[16px] text-[#aaaaaa]">Please confirm your country code</p> 
       <p className="text-[16px] text-[#aaaaaa]">and enter your phone number.</p>
       <form className="flex flex-col mt-[40px] gap-[20px]">
         <CountrySelect onCountryChange = {handleCountryChange} />
         <PhoneNumberInput primaryPhone = {countryPhone}/>
         <button type="submit" className="w-[360px] h-[54px] bg-[#8774e1] rounded-[10px] font-bold">NEXT</button>
       </form>
       <p className="text-[#8774e1] mt-[40px]">LOG IN BY QR CODE</p>
    </div>
  )
}