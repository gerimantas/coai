import { Skeleton } from "@/components/ui/Skeleton"

export const StatCardSkeleton = () => (
  <div className="space-y-3">
    <Skeleton className="h-4 w-[100px]" />
    <Skeleton className="h-8 w-[60px]" />
    <Skeleton className="h-3 w-[120px]" />
  </div>
)

export const ChartSkeleton = () => (
  <div className="space-y-3">
    <Skeleton className="h-4 w-[150px]" />
    <Skeleton className="h-[200px] w-full" />
  </div>
)

export const TableSkeleton = ({ rows = 5 }) => (
  <div className="space-y-2">
    {Array.from({ length: rows }).map((_, i) => (
      <div key={i} className="flex justify-between items-center">
        <Skeleton className="h-4 w-[120px]" />
        <Skeleton className="h-6 w-[80px] rounded-full" />
      </div>
    ))}
  </div>
)

export const LoadingSpinner = ({ size = "md" }) => {
  const sizeClasses = {
    sm: "w-4 h-4",
    md: "w-6 h-6", 
    lg: "w-8 h-8"
  }
  
  return (
    <div className={`animate-spin rounded-full border-2 border-gray-300 border-t-blue-600 ${sizeClasses[size]}`}></div>
  )
}
