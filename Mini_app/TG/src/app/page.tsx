import PhoneLogin from "./Dashboards/phoneLogin";
import QrLogin from "./Dashboards/qrLogin";
export default function Home() {
  return (
    <div className="my-[48px] w-full mx-auto h-[100%] md:w-[720px]">
       <PhoneLogin />
       <QrLogin />
    </div>
  );
}
