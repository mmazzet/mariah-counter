import React from "react";

type MetricBlockProps = {
  label: string;
  value: number;
};

const MetricBlock: React.FC<MetricBlockProps> = ({ label, value }) => {
  return (
    <div className="mb-4 p-2 border">
      <p className="text-sm">{label}</p>
      <p className="text-base font-medium">{value}</p>
    </div>
  );
};

export default MetricBlock;