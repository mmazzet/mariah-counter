import { useEffect, useState } from "react";

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
        console.log("Earnings from backend:", data);
        setEarnings(data);
      })
      .catch((err) => {
        console.error(err);
        setError(err.message);
      });
  }, []);

  if (error) {
    return <div>Error: {error}</div>;
  }

  if (!earnings) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h1>Mariah Carey Earnings</h1>

      <p>Today: {earnings.today_earnings}</p>
      <p>Since Nov 1, 2025: {earnings.since_nov1_2025}</p>
      <p>Total: {earnings.total_earnings}</p>
    </div>
  );
}

export default App;
