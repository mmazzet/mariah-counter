import React from "react";

import AnimatedNumber from "./AnimatedNumber";

type MetricBlockProps = {
  label: string;
  value: number;
};

const MetricBlock: React.FC<MetricBlockProps> = ({ label, value }) => {
  return (
    <div className="mb-4 rounded-lg bg-green-100 p-4 shadow-sm">
      <p className="text-sm font-festive text-gray-600">{label}</p>
      <p className="text-xl font-semibold text-center text-red-500 flex items-center justify-center gap-1">
        $<AnimatedNumber value={value} />
      </p>
    </div>
  );
};

export default MetricBlock;