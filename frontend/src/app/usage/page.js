"use client"

import { useState, useEffect } from 'react'
import PageContainer from "@/components/ui/PageContainer"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/Card"
import { Badge } from "@/components/ui/Badge"
import { Button } from "@/components/ui/Button"

const UsagePage = () => {
  const [usageStats, setUsageStats] = useState(null)
  const [dailySummary, setDailySummary] = useState(null)
  const [loading, setLoading] = useState(true)
  const [statsPeriod, setStatsPeriod] = useState(7)

  useEffect(() => {
    fetchUsageData()
  }, [statsPeriod])

  const fetchUsageData = async () => {
    try {
      setLoading(true)
      const response = await fetch(`/api/usage/stats?days=${statsPeriod}`)
      if (response.ok) {
        const data = await response.json()
        setUsageStats(data.stats)
      }
    } catch (error) {
      console.error('Error fetching usage stats:', error)
    } finally {
      setLoading(false)
    }
  }

  const exportData = async (format) => {
    try {
      const endDate = new Date().toISOString().split('T')[0]
      const startDate = new Date(Date.now() - statsPeriod * 24 * 60 * 60 * 1000).toISOString().split('T')[0]
      
      const response = await fetch('/api/usage/export', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          start_date: startDate,
          end_date: endDate,
          format: format
        })
      })
      
      if (response.ok) {
        const data = await response.json()
        window.open(data.download_url, '_blank')
      }
    } catch (error) {
      console.error('Error exporting data:', error)
    }
  }

  if (loading && !usageStats) {
    return (
      <PageContainer title="Usage Analytics" subtitle="Monitor system usage, costs, and performance">
        <div className="text-center">Loading usage analytics...</div>
      </PageContainer>
    )
  }

  return (
    <PageContainer title="Usage Analytics" subtitle="Monitor system usage, costs, and performance">
      <div className="space-y-6">
        
        {/* Control Panel */}
        <div className="flex justify-between items-center">
          <div className="flex gap-2">
            {[7, 14, 30].map((days) => (
              <Button
                key={days}
                variant={statsPeriod === days ? "default" : "outline"}
                onClick={() => setStatsPeriod(days)}
                size="sm"
              >
                Last {days} days
              </Button>
            ))}
          </div>
          <div className="flex gap-2">
            <Button onClick={() => exportData('json')} variant="outline" size="sm">
              Export JSON
            </Button>
            <Button onClick={() => exportData('csv')} variant="outline" size="sm">
              Export CSV
            </Button>
          </div>
        </div>

        {/* Summary Cards */}
        {usageStats ? (
          <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
            <Card>
              <CardHeader className="pb-2">
                <CardTitle className="text-sm font-medium">Total Requests</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="text-2xl font-bold">{usageStats.totals.requests}</div>
                <p className="text-xs text-gray-600">
                  {usageStats.averages.requests_per_day.toFixed(1)} per day avg
                </p>
              </CardContent>
            </Card>

            <Card>
              <CardHeader className="pb-2">
                <CardTitle className="text-sm font-medium">Total Tokens</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="text-2xl font-bold">{usageStats.totals.tokens.toLocaleString()}</div>
                <p className="text-xs text-gray-600">
                  {usageStats.averages.tokens_per_day.toFixed(0)} per day avg
                </p>
              </CardContent>
            </Card>

            <Card>
              <CardHeader className="pb-2">
                <CardTitle className="text-sm font-medium">Estimated Cost</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="text-2xl font-bold">${usageStats.totals.cost.toFixed(4)}</div>
                <p className="text-xs text-gray-600">
                  ${usageStats.averages.cost_per_day.toFixed(4)} per day avg
                </p>
              </CardContent>
            </Card>

            <Card>
              <CardHeader className="pb-2">
                <CardTitle className="text-sm font-medium">Avg Response Time</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="text-2xl font-bold">{usageStats.averages.response_time.toFixed(2)}s</div>
                <p className="text-xs text-gray-600">
                  {usageStats.totals.real_ai_requests} real AI requests
                </p>
              </CardContent>
            </Card>
          </div>
        ) : (
          <Card>
            <CardContent className="text-center py-8">
              <p className="text-gray-600">No usage data available</p>
              <p className="text-sm text-gray-400 mt-2">Start using the chat feature to see analytics</p>
            </CardContent>
          </Card>
        )}

        {/* Detailed Usage Info */}
        {usageStats && (
          <>
            {/* Agent Usage */}
            <Card>
              <CardHeader>
                <CardTitle>Agent Usage</CardTitle>
                <CardDescription>Distribution of AI agent usage</CardDescription>
              </CardHeader>
              <CardContent>
                <div className="space-y-2">
                  {Object.entries(usageStats.trends.agent_usage).map(([agent, count]) => (
                    <div key={agent} className="flex justify-between items-center">
                      <span className="capitalize">{agent}</span>
                      <Badge variant="secondary">{count} requests</Badge>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>

            {/* Most Active Projects */}
            {usageStats.trends.most_active_projects.length > 0 && (
              <Card>
                <CardHeader>
                  <CardTitle>Most Active Projects</CardTitle>
                  <CardDescription>Projects with highest usage</CardDescription>
                </CardHeader>
                <CardContent>
                  <div className="space-y-2">
                    {usageStats.trends.most_active_projects.slice(0, 10).map(([project, count]) => (
                      <div key={project} className="flex justify-between items-center">
                        <span className="truncate max-w-xs">{project}</span>
                        <Badge variant="outline">{count} requests</Badge>
                      </div>
                    ))}
                  </div>
                </CardContent>
              </Card>
            )}

            {/* Daily Summaries */}
            {usageStats.daily_summaries.length > 0 && (
              <Card>
                <CardHeader>
                  <CardTitle>Daily Breakdown</CardTitle>
                  <CardDescription>Usage statistics by day</CardDescription>
                </CardHeader>
                <CardContent>
                  <div className="space-y-3">
                    {usageStats.daily_summaries.slice(0, 7).map((day) => (
                      <div key={day.date} className="border rounded-lg p-3">
                        <div className="flex justify-between items-center mb-2">
                          <span className="font-medium">{day.date}</span>
                          <Badge variant={day.total_requests > 0 ? "default" : "outline"}>
                            {day.total_requests} requests
                          </Badge>
                        </div>
                        <div className="grid grid-cols-2 md:grid-cols-4 gap-2 text-sm text-gray-600">
                          <div>Tokens: {day.total_tokens}</div>
                          <div>Cost: ${day.total_cost.toFixed(4)}</div>
                          <div>Avg Time: {day.avg_response_time.toFixed(2)}s</div>
                          <div>Success: {day.successful_requests}/{day.total_requests}</div>
                        </div>
                      </div>
                    ))}
                  </div>
                </CardContent>
              </Card>
            )}
          </>
        )}
      </div>
    </PageContainer>
  )
}

export default UsagePage;
