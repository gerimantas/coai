// Centralizuotas puslapio wrapper komponentas
export default function PageContainer({ children }) {
  return (
    <div className="mt-[2%] mr-[2%] px-6 py-6 w-full">
      <div className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-lg p-6 w-full">
        {children}
      </div>
    </div>
  );
}
