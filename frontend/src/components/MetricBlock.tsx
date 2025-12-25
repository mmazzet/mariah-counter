import React from "react";

import AnimatedNumber from "./AnimatedNumber";

type MetricBlockProps = {
  label: string;
  value: number;
};

const MetricBlock: React.FC<MetricBlockProps> = ({ label, value }) => {
  return (
    <div className="mb-4 rounded-lg bg-pink-100 p-4 shadow-sm">
      <p className="text-sm text-gray-600">{label}</p>
      <p className="text-xl font-semibold text-center text-red-500">
        $<AnimatedNumber value={value} />
      </p>
    </div>
  );
};

export default MetricBlock;