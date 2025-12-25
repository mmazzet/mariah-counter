import React, { useEffect, useState } from "react";

type AnimatedNumberProps = {
  value: number;
  duration?: number;
};

const AnimatedNumber: React.FC<AnimatedNumberProps> = ({ value, duration = 1000 }) => {
  const [displayValue, setDisplayValue] = useState(0);

  useEffect(() => {
    let start = 0;
    const increment = value / (duration / 16);
    const interval = setInterval(() => {
      start += increment;
      if (start >= value) {
        start = value;
        clearInterval(interval);
      }
      setDisplayValue(Math.floor(start));
    }, 16);

    return () => clearInterval(interval);
  }, [value, duration]);

  return <>{displayValue.toLocaleString("en-US")}</>;
};

export default AnimatedNumber;