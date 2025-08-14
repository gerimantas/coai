import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/Card"
import { Badge } from "@/components/ui/Badge"
// Temporarily remove lucide-react imports due to React 19 compatibility
// import { TrendingUp, TrendingDown, Clock, DollarSign, Activity, Users } from 'lucide-react'

const getMetricIcon = (type) => {
  const icons = {
    requests: '📊',
    tokens: '🔤',
    cost: '💰',
    time: '⏱️'
  }
  return icons[type] || '📊'
}

const getMetricColor = (type) => {
  const colors = {
    requests: 'text-blue-600',
    tokens: 'text-green-600', 
    cost: 'text-yellow-600',
    time: 'text-purple-600'
  }
  return colors[type] || 'text-gray-600'
}

export const MetricCard = ({ 
  title, 
  value, 
  subtitle, 
  trend, 
  type = 'requests',
  isLoading = false,
  className = ""
}) => {
  const Icon = getMetricIcon(type)
  const iconColor = getMetricColor(type)
  
  if (isLoading) {
    return (
      <Card className={`relative overflow-hidden ${className}`}>
        <CardHeader className="pb-2">
          <div className="flex justify-between items-center">
            <div className="h-4 bg-gray-200 rounded animate-pulse w-24"></div>
            <div className="h-5 w-5 bg-gray-200 rounded animate-pulse"></div>
          </div>
        </CardHeader>
        <CardContent>
          <div className="h-8 bg-gray-200 rounded animate-pulse w-16 mb-2"></div>
          <div className="h-3 bg-gray-200 rounded animate-pulse w-32"></div>
        </CardContent>
      </Card>
    )
  }

  return (
    <Card className={`relative overflow-hidden hover:shadow-md transition-shadow duration-200 ${className}`}>
      <CardHeader className="pb-2">
        <div className="flex justify-between items-center">
          <CardTitle className="text-sm font-medium text-gray-700">{title}</CardTitle>
          <span className={`text-xl ${iconColor}`}>{Icon}</span>
        </div>
      </CardHeader>
      <CardContent>
        <div className="flex items-end justify-between">
          <div>
            <div className="text-2xl font-bold text-gray-900">{value}</div>
            {subtitle && (
              <p className="text-xs text-gray-600 mt-1">{subtitle}</p>
            )}
          </div>
          
          {trend && (
            <div className={`flex items-center gap-1 text-sm ${
              trend.direction === 'up' ? 'text-green-600' : 
              trend.direction === 'down' ? 'text-red-600' : 'text-gray-500'
            }`}>
              {trend.direction === 'up' && <span>📈</span>}
              {trend.direction === 'down' && <span>📉</span>}
              <span>{trend.value}</span>
            </div>
          )}
        </div>
        
        {/* Progress bar for visual context */}
        {trend && trend.percentage && (
          <div className="mt-3">
            <div className="w-full bg-gray-200 rounded-full h-1">
              <div 
                className={`h-1 rounded-full transition-all duration-500 ${
                  trend.direction === 'up' ? 'bg-green-500' : 'bg-red-500'
                }`}
                style={{ width: `${Math.min(trend.percentage, 100)}%` }}
              ></div>
            </div>
          </div>
        )}
      </CardContent>
    </Card>
  )
}

export const StatsGrid = ({ stats, isLoading = false }) => {
  if (!stats && !isLoading) {
    return (
      <Card>
        <CardContent className="text-center py-8">
          <span className="text-4xl text-gray-400 mb-4 block">📊</span>
          <p className="text-gray-600 mb-2">No usage data available</p>
          <p className="text-sm text-gray-400">Start using the chat feature to see analytics</p>
        </CardContent>
      </Card>
    )
  }

  const metrics = [
    {
      title: "Total Requests",
      value: stats?.totals?.requests || 0,
      subtitle: `${(stats?.averages?.requests_per_day || 0).toFixed(1)} per day avg`,
      type: "requests"
    },
    {
      title: "Total Tokens", 
      value: (stats?.totals?.tokens || 0).toLocaleString(),
      subtitle: `${(stats?.averages?.tokens_per_day || 0).toFixed(0)} per day avg`,
      type: "tokens"
    },
    {
      title: "Estimated Cost",
      value: `$${(stats?.totals?.cost || 0).toFixed(4)}`,
      subtitle: `$${(stats?.averages?.cost_per_day || 0).toFixed(4)} per day avg`,
      type: "cost"
    },
    {
      title: "Avg Response Time",
      value: `${(stats?.averages?.response_time || 0).toFixed(2)}s`,
      subtitle: `${stats?.totals?.real_ai_requests || 0} real AI requests`,
      type: "time"
    }
  ]

  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
      {metrics.map((metric, index) => (
        <MetricCard
          key={metric.title}
          title={metric.title}
          value={metric.value}
          subtitle={metric.subtitle}
          type={metric.type}
          isLoading={isLoading}
          className="transform transition-transform duration-200 hover:scale-105"
        />
      ))}
    </div>
  )
}
