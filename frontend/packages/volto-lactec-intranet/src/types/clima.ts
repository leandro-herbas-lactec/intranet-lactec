export type ClimaData = {
  '@id': string;
  events: {
    sunrise: string;
    sunset: string;
  };
  temperature: {
    hourly: Record<string, number>;
    now: number;
  };
  weather: string;
};
