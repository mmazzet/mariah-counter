import { useEffect, useState } from "react";
import MetricBlock from "./components/MetricBlock";
import Snow from "./components/Snow";

type Earnings = {
  today_earnings: number;
  since_nov1_2025: number;
  total_earnings: number;
};

function App() {
  const [earnings, setEarnings] = useState<Earnings | null>(null);
  const [error, setError] = useState<string | null>(null);
  

  useEffect(() => {
    fetch("http://localhost:8000/earnings")
      .then((res) => {
        if (!res.ok) {
          throw new Error("Failed to fetch earnings");
        }
        return res.json();
      })
      .then((data: Earnings) => {
        setEarnings(data);
      })
      .catch((err) => {
        console.error(err);
        setError(err.message);
      });
  }, []);

  if (error) {
    return <div className="p-4">Error: {error}</div>;
  }

  if (!earnings) {
    return (
      <div className="p-4 space-y-4">
        <div className="h-16 rounded-lg bg-gray-200 animate-pulse"></div>
        <div className="h-16 rounded-lg bg-gray-200 animate-pulse"></div>
        <div className="h-16 rounded-lg bg-gray-200 animate-pulse"></div>
      </div>
    );
  }

  return (
    <div className="relative z-10">
       <Snow />
      {/* Header */}
      <h1 className="mb-6 text-4xl font-bold  text-red-500 font-festive flex items-center gap-2">
        <img src="/src/assets/image-header-its-time.jpg" alt="Mariah Carey" className="h-20 w-20 rounded-full" />
        Mariah Carey Earnings
      </h1>

      {/* Metrics */}
      <MetricBlock label="Today" value={earnings.today_earnings} />
      <MetricBlock label="Earnings since 1st November 2025" value={earnings.since_nov1_2025} />
      <MetricBlock label="Total Earnings since 1994" value={earnings.total_earnings} />
    </div>
  );
  }

export default App;
