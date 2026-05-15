# aws-mcp-nordstan-agent

feat: implement MCP restaurant search architecture on AWS ECS/Fargate with Lambda integration

- created MCP server using FastMCP
- implemented search_restaurants MCP tool
- integrated boto3 Lambda invocation
- created nordstan-lambda restaurant backend
- containerized MCP server with Docker and uv
- pushed container image to ECR
- created ECS Fargate cluster/service/task definition
- configured ECS task role and execution role
- configured CloudWatch logging
- exposed MCP server on port 8000
- verified MCP endpoint locally with uvicorn
- identified localhost binding issue (127.0.0.1 vs 0.0.0.0)