type Snowflake = {
  left: string;
  delay: string;
  duration: string;
  size: string;
};

const snowflakes: Snowflake[] = Array.from({ length: 30 }).map(() => ({
  left: `${Math.random() * 100}%`,
  delay: `${Math.random() * 10}s`,
  duration: `${10 + Math.random() * 10}s`,
  size: `${8 + Math.random() * 10}px`,
}));

const Snow = () => {
  return (
    <div className="pointer-events-none fixed inset-0 z-0 overflow-hidden">
      {snowflakes.map((flake, i) => (
        <span
          key={i}
          className="snowflake"
          style={{
            left: flake.left,
            animationDelay: flake.delay,
            animationDuration: flake.duration,
            fontSize: flake.size,
          }}
        >
          ❄️
        </span>
      ))}
    </div>
  );
};

export default Snow;