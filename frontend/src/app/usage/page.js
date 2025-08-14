"use client"

import PageContainer from "@/components/ui/PageContainer"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/Card"
import { Badge } from "@/components/ui/Badge"
import { Alert, AlertDescription } from "@/components/ui/Alert"
import { UsageChart } from "@/components/analytics/UsageChart"
import { AnalyticsControls } from "@/components/analytics/AnalyticsControls"
import { StatsGrid } from "@/components/analytics/MetricCard"
import { StatCardSkeleton, ChartSkeleton, TableSkeleton } from "@/components/analytics/LoadingComponents"
import useUsageAnalytics from "@/hooks/useUsageAnalytics"

const UsagePage = () => {
  const {
    usageStats,
    loading,
    error,
    statsPeriod,
    lastUpdated,
    autoRefresh,
    setAutoRefresh,
    refreshData,
    exportData,
    changePeriod
  } = useUsageAnalytics()

  // Prepare chart data
  const chartData = usageStats?.daily_summaries?.map(day => ({
    date: day.date,
    requests: day.total_requests,
    tokens: day.total_tokens,
    cost: day.total_cost,
    avgTime: day.avg_response_time
  })) || []

  const agentUsageData = usageStats?.trends?.agent_usage ? 
    Object.entries(usageStats.trends.agent_usage).map(([name, value]) => ({ name, value })) : []

  return (
    <PageContainer title="Usage Analytics" subtitle="Monitor system usage, costs, and performance">
      <div className="space-y-6">
        
        {/* Error Alert */}
        {error && (
          <Alert variant="destructive">
            <div className="h-4 w-4 inline-block mr-2">⚠️</div>
            <AlertDescription>
              Failed to load analytics data: {error}
            </AlertDescription>
          </Alert>
        )}
        
        {/* Enhanced Control Panel */}
        <AnalyticsControls
          statsPeriod={statsPeriod}
          setStatsPeriod={changePeriod}
          onRefresh={refreshData}
          onExport={exportData}
          isLoading={loading}
          lastUpdated={lastUpdated}
          autoRefresh={autoRefresh}
          setAutoRefresh={setAutoRefresh}
        />

        {/* Enhanced Summary Cards */}
        <StatsGrid stats={usageStats} isLoading={loading} />

        {/* Enhanced Summary Cards */}
        <StatsGrid stats={usageStats} isLoading={loading} />

        {/* Interactive Charts */}
        {chartData.length > 0 && (
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <Card>
              <CardHeader>
                <CardTitle>Request Trends</CardTitle>
                <CardDescription>Daily request volume over time</CardDescription>
              </CardHeader>
              <CardContent>
                <UsageChart data={chartData} type="line" title="Daily Requests" />
              </CardContent>
            </Card>

            <Card>
              <CardHeader>
                <CardTitle>Agent Distribution</CardTitle>
                <CardDescription>Usage breakdown by AI agent</CardDescription>
              </CardHeader>
              <CardContent>
                {loading ? (
                  <ChartSkeleton />
                ) : (
                  <UsageChart data={agentUsageData} type="pie" title="Agent Usage" />
                )}
              </CardContent>
            </Card>
          </div>
        )}

        {/* Enhanced Detailed Usage Info */}
        {usageStats && (
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            
            {/* Agent Usage */}
            <Card className="hover:shadow-lg transition-shadow duration-200">
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  Agent Usage
                  <Badge variant="secondary">{Object.keys(usageStats.trends.agent_usage).length} agents</Badge>
                </CardTitle>
                <CardDescription>Distribution of AI agent usage</CardDescription>
              </CardHeader>
              <CardContent>
                {loading ? (
                  <TableSkeleton rows={3} />
                ) : (
                  <div className="space-y-3">
                    {Object.entries(usageStats.trends.agent_usage).map(([agent, count]) => (
                      <div key={agent} className="flex justify-between items-center p-3 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors">
                        <span className="capitalize font-medium">{agent}</span>
                        <div className="flex items-center gap-2">
                          <div className="w-20 bg-gray-200 rounded-full h-2">
                            <div 
                              className="bg-blue-600 h-2 rounded-full transition-all duration-500"
                              style={{ width: `${(count / Math.max(...Object.values(usageStats.trends.agent_usage))) * 100}%` }}
                            ></div>
                          </div>
                          <Badge variant="secondary">{count}</Badge>
                        </div>
                      </div>
                    ))}
                  </div>
                )}
              </CardContent>
            </Card>

            {/* Most Active Projects */}
            {usageStats.trends.most_active_projects.length > 0 && (
              <Card className="hover:shadow-lg transition-shadow duration-200">
                <CardHeader>
                  <CardTitle className="flex items-center gap-2">
                    Most Active Projects
                    <Badge variant="secondary">{usageStats.trends.most_active_projects.length} projects</Badge>
                  </CardTitle>
                  <CardDescription>Projects with highest usage</CardDescription>
                </CardHeader>
                <CardContent>
                  {loading ? (
                    <TableSkeleton rows={5} />
                  ) : (
                    <div className="space-y-2">
                      {usageStats.trends.most_active_projects.slice(0, 10).map(([project, count], index) => (
                        <div key={project} className="flex justify-between items-center p-3 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors">
                          <div className="flex items-center gap-3">
                            <div className={`w-6 h-6 rounded-full flex items-center justify-center text-xs font-bold text-white ${
                              index === 0 ? 'bg-yellow-500' : index === 1 ? 'bg-gray-400' : index === 2 ? 'bg-orange-500' : 'bg-blue-500'
                            }`}>
                              {index + 1}
                            </div>
                            <span className="truncate max-w-xs font-medium">{project}</span>
                          </div>
                          <Badge variant="outline">{count} requests</Badge>
                        </div>
                      ))}
                    </div>
                  )}
                </CardContent>
              </Card>
            )}
          </div>
        )}

        {/* Enhanced Daily Summaries */}
        {usageStats?.daily_summaries?.length > 0 && (
          <Card className="hover:shadow-lg transition-shadow duration-200">
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                Daily Breakdown
                <Badge variant="secondary">{usageStats.daily_summaries.length} days</Badge>
              </CardTitle>
              <CardDescription>Detailed usage statistics by day</CardDescription>
            </CardHeader>
            <CardContent>
              {loading ? (
                <div className="space-y-3">
                  {Array.from({ length: 7 }).map((_, i) => (
                    <div key={i} className="border rounded-lg p-4">
                      <div className="flex justify-between items-center mb-3">
                        <div className="h-4 bg-gray-200 rounded animate-pulse w-24"></div>
                        <div className="h-6 bg-gray-200 rounded-full animate-pulse w-20"></div>
                      </div>
                      <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
                        {Array.from({ length: 4 }).map((_, j) => (
                          <div key={j} className="h-3 bg-gray-200 rounded animate-pulse"></div>
                        ))}
                      </div>
                    </div>
                  ))}
                </div>
              ) : (
                <div className="space-y-3">
                  {usageStats.daily_summaries.slice(0, 7).map((day) => (
                    <div key={day.date} className="border rounded-lg p-4 hover:bg-gray-50 transition-colors">
                      <div className="flex justify-between items-center mb-3">
                        <span className="font-medium text-lg">{day.date}</span>
                        <div className="flex items-center gap-2">
                          <Badge variant={day.total_requests > 0 ? "default" : "outline"}>
                            {day.total_requests} requests
                          </Badge>
                          {day.total_requests > 0 && (
                            <div className={`w-3 h-3 rounded-full ${
                              day.total_requests > 10 ? 'bg-green-500' : 
                              day.total_requests > 5 ? 'bg-yellow-500' : 'bg-blue-500'
                            }`}></div>
                          )}
                        </div>
                      </div>
                      <div className="grid grid-cols-2 md:grid-cols-4 gap-3 text-sm">
                        <div className="flex flex-col">
                          <span className="text-gray-500">Tokens</span>
                          <span className="font-semibold">{day.total_tokens.toLocaleString()}</span>
                        </div>
                        <div className="flex flex-col">
                          <span className="text-gray-500">Cost</span>
                          <span className="font-semibold">${day.total_cost.toFixed(4)}</span>
                        </div>
                        <div className="flex flex-col">
                          <span className="text-gray-500">Avg Time</span>
                          <span className="font-semibold">{day.avg_response_time.toFixed(2)}s</span>
                        </div>
                        <div className="flex flex-col">
                          <span className="text-gray-500">Success Rate</span>
                          <span className="font-semibold">
                            {day.total_requests > 0 ? ((day.successful_requests / day.total_requests) * 100).toFixed(1) : 0}%
                          </span>
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </CardContent>
          </Card>
        )}
      </div>
    </PageContainer>
  )
}

export default UsagePage;
